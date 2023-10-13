import pytest
from django.urls import reverse

from lessons.admin import LessonAdmin


pytestmark = [
    pytest.mark.django_db,
]


def test_view(admin_client, django_assert_num_queries, lessons):
    url = reverse('admin:lessons_lesson_changelist')
    try:
        with django_assert_num_queries(5):
            admin_client.get(url)
    except pytest.fail.Exception as e:
        raise AssertionError(
            'Make sure that, when displaying the sets of lessons in the `LessonAdmin` admin panel, '
            'the request optimization is used according to the task.'
        ) from e

    assert getattr(LessonAdmin, 'list_select_related') == ('course', ), (
        'Make sure that the request optimization of the sets of lessons in the `LessonAdmin` admin panel '
        'corresponds to the task.'
    )


def test_lesson_name(admin_client, lessons):
    assert hasattr(LessonAdmin, 'lesson_name'), (
        'Make sure that the method `lesson_name` in `LessonAdmin` is declared according to the task.'
    )
    assert getattr(LessonAdmin.lesson_name, 'short_description', None) == 'Lesson title', (
        'Make sure the method `lesson_name` in `LessonAdmin` '
        'has the required attribute `short_description` according to the task.'
    )

    url = reverse('admin:lessons_lesson_changelist')
    response = admin_client.get(url)
    list_lesson_names = [
        f'{lesson.course}: {lesson}' for lesson in lessons
    ]
    content = response.content.decode('utf-8')
    for lesson_name in list_lesson_names:
        assert lesson_name in content, (
            'Make sure the method `lesson_name` in `LessonAdmin` '
            'returns the value according to the task.'
        )
