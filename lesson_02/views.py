import os
from datetime import datetime

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
    if request.get('method') == 'POST':
        now = datetime.now()
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{path}/messages/message_{now.strftime("%d%m%Y")}_{now.strftime("%H.%M.%S")}.txt', 'w') as message_file:
            message_file.write(f'Нам пришло сообщение от {email} с темой \n {title} \n и текстом \n {text}')
        return '200 OK', render_('contacts.html')
    else:
        return '200 OK', render_('contacts.html')


def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 not found!']
