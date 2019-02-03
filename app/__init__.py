from flask import Flask

# Initializinng application
app = Flask(__name__)

from app import views
