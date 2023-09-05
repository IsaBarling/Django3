from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def text(title, text):
    return f'<h1>Мой сайт</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'


def index(request):
    title = 'Главная'
    body_text = 'Это мой первый Django-сайт'
    logger.info(f'Page "general" is open')
    return HttpResponse(text(title, body_text))


def about(request):
    title = 'О себе'
    body_text = 'Привет, я Student Developer, я умею писать "Hello World" <br>' \
                'Здесь обычно располагаются контакты'
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
