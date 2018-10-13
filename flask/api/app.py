import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
env = os.getenv('FLASK_ENV', 'development')

@app.route('/')
def hello_world():
    return "Hello World!"

def create_app():
    return app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
