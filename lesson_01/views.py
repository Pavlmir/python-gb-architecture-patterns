from framework.templates import render_


def index_view(request):
    data = {'name_company': 'ООО Сладкоежка',
            'products': ['Шоколадки', 'Пончики', 'Халва']}

    return '200 OK', render_('index.html', **data)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', render_('about.html')


def contact_view(request):
    # Проверка метода запроса
    return '200 OK', render_('contacts.html')


def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 not found!']
