from flask import request
from database.models import Books, User
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token

class RegisterAPI(Resource):
    
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
    
class LoginAPI(Resource):
    
    def post(self):
        body = request.get_json()
        user = User.objects.get(email = body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Invalid Credentials'}, 401
        expiry = datetime.timedelta(days=1)
        accesss_token = create_access_token(identity=str(user.id), expires_delta=expiry)
        return {'token': accesss_token}, 200