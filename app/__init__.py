from flask import Flask

app = Flask(__name__)
app.secret_key = "carol123"
from app.controllers import auth_controller
