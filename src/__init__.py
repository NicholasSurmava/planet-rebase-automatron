import os
from flask import Flask, jsonify, redirect, url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return redirect(url_for('fe.dashboard'))

    @app.route('/heartbeat')
    def heartbeat():
        return jsonify({
            "heartbeat": "badum badum badum"
        })

    from .api.v1 import api
    from .frontend import fe

    app.register_blueprint(api)
    app.register_blueprint(fe)

    return app
