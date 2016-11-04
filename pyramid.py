from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def index(request):
    return Response("""<a href="index.html">Относительная</a> | <a href="C:/WebServers/home/myproject/index.html">Абсолютная</a>""")
def about(request):
    return Response("""<a href="about/aboutme.html">Относительная</a> | <a href="C:/WebServers/home/myproject/about/abotme.html">Абсолютная</a>""")

if __name__ == '__main__':
    config = Configurator()
    config.add_route('index', '/')
    config.add_view(index, route_name='index')
    config.add_route('about', 'about')
    config.add_view(about, route_name='about')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
