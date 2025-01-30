from flask import Flask
from frontend import frontend
from backend import backend

app = Flask(__name__)
app.secret_key = 'saurons_ring_secret'

# Register Blueprints
app.register_blueprint(frontend, url_prefix='/')  # Frontend routes
app.register_blueprint(backend, url_prefix='/backend')  # Backend routes

if __name__ == '__main__':
    app.run(debug=True)
