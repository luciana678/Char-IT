import flask
from src.web.controllers import root

_blueprints = (
    root.bp
)

def init_app(app: flask.Flask):
    """Initializes the controllers.
    Registers the blueprints and error handlers for the application.
    Also registers the before request hook for the application.
    """

    app.register_blueprint(_blueprints)



