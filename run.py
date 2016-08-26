from flask import Flask
from rest.api_base import rest_api


app = Flask(__name__)
app.DEBUG = True
app.SECRET_KEY = 'development-secret-key'
app.register_blueprint(rest_api)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
