from flask import Blueprint, render_template, request, current_app, flash, redirect, url_for
from flask_mail import Mail, Message
from src.core.models.database import db
from src.web.formularios.registrar_colaborador import RegistrarColbForm
from src.core.models.usuario import Usuario
import secrets
from flask import (
    Blueprint,
    render_template
)

bp = Blueprint("registrarColaborador", __name__)

@bp.route("/registrarColaborador", methods=['GET','POST'])
def registrarColaborador():
    form = RegistrarColbForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        # Verifica si el correo electrónico ya está registrado
        existing_user = Usuario.query.filter_by(email=email).first()
        if existing_user:
            flash_message='Usted ya se encuentra registrado.'
        else:
            flash_message='Usuario registrado Correctamente!. Se ha enviado un correo electrónico con la contraseña.'
            contraseña = secrets.token_urlsafe(8)
            new_user = Usuario(nombre=nombre, apellido=apellido, email=email, password=contraseña, id_rol=2)
            db.session.add(new_user)
            db.session.commit()
            send_mail(new_user.id)
        flash(flash_message, 'success')              
        return redirect(url_for('root.usuarios_colaboradores_get'))  # Redirige a la página correspondiente
    return render_template("owner/registrarColaborador.html", form=form)


def send_mail(userId: int)->None:
    """
    Send the confirmation email to the user.
    """
    app = current_app._get_current_object()
    usuario = Usuario.query.get(userId)
    mail = Mail(app)
    subject = 'Confirmación de Registro'
    sender = app.config['MAIL_DEFAULT_SENDER']
    recipients = [usuario.email]
    message = f'¡Felicidades! Tu registro ha sido exitoso. La contraseña para ingresar es:\n\n {usuario.password} \n\n Recorda Cambiar tu contraseña en tu primer ingreso. '
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = message

    mail.send(msg)