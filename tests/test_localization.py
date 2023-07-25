import importlib

import pytest


@pytest.mark.parametrize(('n_app', 'n_model', 'param', 'text'), [
    (
        'courses',
        'Course',
        'is_public',
        'Установите галочку, чтобы сделать курс публичным.'
    ),
    (
        'courses',
        'Category',
        'slug',
        'Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    ),
    (
        'lessons',
        'Lesson',
        'duration',
        'Укажите продолжительность курса в минутах.'
    )
])
def test_help_text_translate(n_app, n_model, param, text):
    module = importlib.import_module(f'{n_app}.models')
    model = getattr(module, n_model)
    field = model._meta.get_field(param)
    assert field.help_text == text, (
        f'Убедитесь, что в приложении `{n_app}` в модели `{n_model}` значение `help_text` '
        f'для атрибута `{param}` '
        'установлено в соответствии с заданием.'
    )
