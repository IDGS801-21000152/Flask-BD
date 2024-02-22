
from config import DevelopmentConfig

from flask import Flask, render_template, request
from flask import flash
from flask import g
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    csrf.init_app(app)
    app.run()