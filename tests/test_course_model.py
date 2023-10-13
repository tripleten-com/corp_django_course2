import pytest
from django.db.models import (
    BooleanField, CharField, DateTimeField, ForeignKey, TextField)
from django.db.utils import IntegrityError

from courses.models import Course
from tests.conftest import _TestModelAttrs

pytestmark = [
    pytest.mark.django_db,
]


@pytest.mark.parametrize(('field', 'type', 'params'), [
    ('title', CharField, {'max_length': 256}),
    ('description', TextField, {}),
    ('author', ForeignKey, {'null': False}),
    ('category', ForeignKey, {'null': False}),
    ('is_public', BooleanField, {'default': False}),
    ('created_at', DateTimeField, {'auto_now_add': True}),
    ('updated_at', DateTimeField, {'auto_now': True}),
])
class TestCategoryModelAttrs(_TestModelAttrs):

    @property
    def model(self):
        return Course


def test__str__(mixer):
    app_label = 'courses'
    model_name = 'Course'
    title = 'Test course title'

    obj = mixer.blend(f'{app_label}.{model_name}', title=title)
    assert str(obj) == title, (
        f'Make sure the model `{model_name}` '
        'has readable object names that correspond to the task.'
    )


def test_author_on_delete(courses_with_author):
    author = courses_with_author[0].author
    try:
        author.delete()
    except IntegrityError:
        raise AssertionError(
            'Make sure that the value of the attribute `on_delete`,  '
            'belonging to the field `author` in the `Course` model, matches the task.'
        )
    assert not Course.objects.filter(author=author).exists(),  (
        'Make sure that the value of the attribute `on_delete`,  '
        'belonging to the field `author` in the `Course` model, matches the task.'
    )


def test_category_on_delete(courses_with_category):
    category = courses_with_category[0].category
    try:
        category.delete()
    except IntegrityError:
        raise AssertionError(
            'Make sure that the value of the attribute `on_delete`,  '
            'belonging to the field `category` in the `Course` model, matches the task.'
        )
    assert not Course.objects.filter(category=category).exists(), (
        'Make sure that the value of the attribute `on_delete`,  '
        'belonging to the field `category` in the `Course` model, matches the task.'
    )
