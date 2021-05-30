from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from routes import initialize_route
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app= Flask(__name__)
api = Api(app)

DB_ATLAS_URI = "mongodb+srv://khushi:Password123!@cluster0.qazna.mongodb.net/python_test?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_ATLAS_URI
app.config["JWT_SECRET_KEY"] = 'cst-authorization'

initialize_db(app)
initialize_route(api)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run()