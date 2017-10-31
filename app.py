# """Hello World."""
# from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
# from pyramid.response import Response


# def hello_world(request):
#     """The first view."""
#     return Response('Hello World!')


# if __name__ == '__main__':
#     config = Configurator()
#     config.add_route('hello', '/')
#     config.add_view(hello_world, route_name='hello')
#     app = config.make_wsgi_app()
#     server = make_server('127.0.0.1', 6543, app)
#     server.serve_forever()
