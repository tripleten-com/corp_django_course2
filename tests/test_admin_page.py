import pytest

from django.apps import apps
from django.contrib import admin

from lessons.models import Lesson


@pytest.mark.parametrize(
    'app_label, model_name, config_attrs',
    [
        (
            'courses',
            'Category',
            {
                'list_display': ('title', 'description',),
                'search_fields': ('title', 'description__contains',),
                'list_display_links': ('title',),
            },
        ),
        (
            'courses',
            'Course',
            {
                'list_display': ('title', 'author', 'category', 'is_public',),
                'list_filter': ('category', 'is_public',),
                'list_editable': ('is_public',),
                'list_display_links': ('title',),
                'readonly_fields': ('created_at', 'updated_at',),
            }
        ),
        (
            'lessons',
            'Lesson',
            {
                'list_display': ('lesson_name', 'type', 'duration',),
                'list_filter': ('type',),
                'list_display_links': ('lesson_name',),
                'list_editable': ('duration',)
            },
        ),
    ]
)
def test_admin_register(app_label, model_name, config_attrs):
    try:
        model = apps.get_model(app_label, model_name)
    except LookupError:
        raise AssertionError(
            f'Make sure the model `{model_name}` is declared in the app `{app_label}`.'
        )
    assert model in admin.site._registry, (
        f'Make sure the model `{model._meta.object_name}` '
        'is registered in the admin panel.'
    )

    site = admin.site._registry[model]
    for attr, value in config_attrs.items():
        actual_value = getattr(site, attr)
        assert actual_value == value, (
            f'Make sure the value of the attribute `{model._meta.object_name}` '
            f'`{attr}` for the model matches the task (check it in the admin panel).'
        )


def test_lesson_inline():
    try:
        from courses.admin import LessonInline
    except ImportError:
        raise AssertionError(
            f'Make sure there is the class `LessonInline`in the file `courses/admin.py`.'
        )

    app_label = 'courses'
    model_name = 'Course'
    try:
        model = apps.get_model(app_label, model_name)
    except LookupError:
        raise AssertionError(
            f'Make sure the model `{model_name}` is declared in the app `{app_label}`.'
        )
    assert model in admin.site._registry, (
        f'Make sure the model `{model._meta.object_name}` '
        'is registered in the admin panel.'
    )

    course_admin_site = admin.site._registry[model]

    assert course_admin_site.inlines == (LessonInline, ), (
        f'Make sure the model `LessonInline` is set up for displaying the related records'
        'в админ представлении модели `Course`.'
    )


@pytest.mark.parametrize(
    'expected_inline_class, config_attrs',
    [
        (admin.StackedInline, {'model': Lesson, 'extra': 0}),
    ]
)
def test_lesson_inline_config(expected_inline_class, config_attrs):
    try:
        from courses.admin import LessonInline
    except ImportError:
        raise AssertionError(
            f'Make sure there is the class `LessonInline`in the file `courses/admin.py`.'
        )

    assert issubclass(LessonInline, expected_inline_class), (
        f'Make sure the class `LessonInline` is inherited accordingly to the task in the file `courses/admin.py`.'
    )

    for attr, value in config_attrs.items():
        actual_value = getattr(LessonInline, attr)
        assert actual_value == value, (
            f'Убедитесь, что в файле `courses/admin.py` для класса `LessonInline` '
            f'The value of the `{attr}` attribute is set according to the task.'
        )
