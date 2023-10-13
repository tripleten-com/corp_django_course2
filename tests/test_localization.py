import importlib

import pytest


@pytest.mark.parametrize(('n_app', 'n_model', 'param', 'text'), [
    (
        'courses',
        'Course',
        'is_public',
        'Put a tick in the corresponding checkbox to make the course public.'
    ),
    (
        'courses',
        'Category',
        'slug',
        'The page identifier for the URL; '
        'allows only Latin letters, numbers, hyphens, and underscores.'
    ),
    (
        'lessons',
        'Lesson',
        'duration',
        'State the course duration in minutes.'
    )
])
def test_help_text_translate(n_app, n_model, param, text):
    module = importlib.import_module(f'{n_app}.models')
    model = getattr(module, n_model)
    field = model._meta.get_field(param)
    assert field.help_text == text, (
        f'Make sure that in the `{n_app}`'s model `{n_model}`, the value of `help_text` '
        f'has the value `{param}` '
        'that matches the task.'
    )
