"""Creates the application. Run it with:

    flask --app app run --debug

The routes themselves are not in this file but in routes/, one file per part
of your application. That way five people rarely edit the same file.
"""

from flask import Flask, render_template

from config import Config
from models import db
from routes.main import bp as main_bp
from routes.classes import bp as classes_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Every file in routes/ is registered here, one line each.
app.register_blueprint(main_bp)
app.register_blueprint(classes_bp)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
