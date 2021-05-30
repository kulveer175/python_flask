from flask import Response, request
from database.models import Books
from flask_restful import Resource
from flask_jwt_extended.view_decorators import jwt_required

class BooksAPI(Resource):

    def get(self):
        book = Books.objects().to_json()
        return Response(book, mimetype="applicaiton/json", status=200)
    
    def post(self):
        body = request.get_json()
        book = Books(**body).save()
        id = book.id
        return {'id': str(id)}, 201
    
    
class SingleBookAPI(Resource):
    
    def get(self, id):
        book = Books.objects.get(b_id=id).to_json()
        return Response(book, mimetype="applicaiton/json", status=200)

    @jwt_required
    def put(self, id):
        body = request.get_json()
        Books.objects.get(b_id=id).update(**body)
        return 'book updated', 200
    
    @jwt_required
    def delete(self, id):
        book = Books.objects.get(b_id=id)
        book.delete()
        return Response("book Deleted Successfully", mimetype="applicaiton/json", status=200)