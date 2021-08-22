from wsgiref.simple_server import make_server

import views
from framework import Application
from datetime import date

routes = {
    '/': views.index_view,
    '/about/': views.about_view,
    '/contacts/': views.contact_view
}


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]
application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
