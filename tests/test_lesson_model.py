import pytest
from django.db.models import (
    CharField, DateTimeField, ForeignKey, TextField, PositiveSmallIntegerField, TextChoices
)
from django.db.utils import IntegrityError

from lessons.models import Lesson
from tests.conftest import _TestModelAttrs

pytestmark = [
    pytest.mark.django_db,
]


@pytest.mark.parametrize(
    'attr, value, label',
    [
        ('EDU', 'edu', 'Programming'),
        ('THEORY', 'theory', 'Theory'),
        ('QUIZ', 'quiz', 'Trivia'),
    ]
)
def test_exists_lesson_type_inner_class(attr, value, label):
    assert hasattr(Lesson, 'LessonType'), (
        'Make sure that in the model `lessons/models.py` '
        'in the `Lesson` model from the `courses/admin.py` file.'
    )

    actual_attr = getattr(Lesson.LessonType, attr, None)
    assert actual_attr is not None and actual_attr.value == value and actual_attr.label == label, (
        'Make sure that in the model `lessons/models.py` '
        f'(the `lessons/models.py` file), the attribute `{attr}` of the class `LessonType` corresponds to the task.'
    )


@pytest.mark.parametrize(('field', 'type', 'params'), [
    ('title', CharField, {'max_length': 256}),
    ('text', TextField, {}),
    ('type', CharField, {'max_length': 16, 'choices': [('edu', 'Programming'), ('theory', 'Theory'), ('quiz', 'Trivia')]}),
    ('duration', PositiveSmallIntegerField, {}),
    ('course', ForeignKey, {'null': False}),
    ('created_at', DateTimeField, {'auto_now_add': True}),
    ('updated_at', DateTimeField, {'auto_now': True}),
])
class TestCategoryModelAttrs(_TestModelAttrs):

    @property
    def model(self):
        return Lesson


def test__str__(mixer):
    app_label = 'lessons'
    model_name = 'Lesson'
    title = 'Test lesson title'
    obj = mixer.blend(f'{app_label}.{model_name}', title=title)

    assert str(obj) == title, (
        f'Make sure the model `{model_name}` '
        'has readable object names that correspond to the task.'
    )


def test_author_on_delete(lessons_with_course):
    course = lessons_with_course[0].course
    try:
        course.delete()
    except IntegrityError:
        raise AssertionError(
            'Make sure that the value of the attribute `on_delete`,  '
            'belonging to the field `course` in the model `Lesson`, corresponds to the task.'
        )
    assert not Lesson.objects.filter(course=course).exists(),  (
        'Make sure that the value of the attribute `on_delete`,  '
        'belonging to the field `course` in the model `Lesson`, corresponds to the task.'
    )
