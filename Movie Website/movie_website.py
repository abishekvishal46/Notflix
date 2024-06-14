from flask import Flask

app = Flask(__name__)

# Import routes (imported at the end to avoid circular import issues)
from routes import *
