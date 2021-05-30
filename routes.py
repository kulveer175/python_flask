from books import BooksAPI, SingleBookAPI
from auth import LoginAPI, RegisterAPI

def initialize_route(api):
    api.add_resource(BooksAPI, '/books')
    api.add_resource(SingleBookAPI, '/books/<id>')
    api.add_resource(RegisterAPI, '/auth/register')
    api.add_resource(LoginAPI, '/auth/login')