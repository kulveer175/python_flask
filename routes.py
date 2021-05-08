from books import BooksAPI, SingleBookAPI

def initialize_route(api):
    api.add_resource(BooksAPI, '/books')
    api.add_resource(SingleBookAPI, '/books/<id>')