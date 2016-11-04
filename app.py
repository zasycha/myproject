from jinja2 import Environment, FileSystemLoader, Template
from wsgiref.simple_server import make_server

headers = [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(content)))
            ]

jenv = Environment(loader=FileSystemLoader('.'))

def app(env, start_resp):
    start_resp('200 OK', headers)
    path = env['PATH_INFO']

    def template(link):
        return jenv.get_template(path).render(link=link)

    if 'index.html' in path:
        link = '<a href="/about/aboutme.html">About me</a>'

    if 'about/aboutme.html' in path:
        link = '<a href="/index.html">Index</a>'

    return [template(link).encode('utf-8')]

serv = make_server("", 8000, app)
serv.serve_forever()
