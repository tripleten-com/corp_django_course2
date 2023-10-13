import pytest
from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, ContentType
from mixer.backend.django import mixer as _mixer

try:
    from courses.models import Category, Course  # noqa:F401
    from lessons.models import Lesson  # noqa:F401
except ImportError as e:
    raise AssertionError(
        f'When importing the models from `{e.name.replace(".", "/")}.py,` '
        f'an error occurred: {e}') from e
except RuntimeError:
    registered_apps = set(app.name for app in apps.get_app_configs())
    need_apps = {'courses': 'courses', 'lessons': 'lessons'}
    if not set(need_apps.values()).intersection(registered_apps):
        need_apps = {
            'courses': 'courses.apps.CoursesConfig', 'lessons': 'lessons.apps.LessonsConfig'}

    for need_app_name, need_app_conf_name in need_apps.items():
        if need_app_conf_name not in registered_apps:
            raise AssertionError(
                f'Make sure the app is registered. {need_app_name}'
            )

pytest_plugins = [
    'fixtures.fixture_data'
]


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def course_permissions():
    content_type = ContentType.objects.get_for_model(Course)
    return Permission.objects.filter(content_type=content_type)


@pytest.fixture
def author(mixer, course_permissions):
    User = get_user_model()
    user = mixer.blend(User, is_staff=True)

    for permission in course_permissions:
        user.user_permissions.add(permission)

    return user


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


class _TestModelAttrs:

    @property
    def model(self):
        raise NotImplementedError(
            'Override this property in inherited test class')

    def get_parameter_display_name(self, param):
        return param

    def test_model_attrs(self, field, type, params):
        model_name = self.model.__name__
        assert hasattr(self.model, field), (
            f'Specify the `{field}` attribute in the model `{model_name}`.')
        model_field = self.model._meta.get_field(field)
        assert isinstance(model_field, type), (
            f'Specify `{type}` of the attribute `{field}` '
            f'in the model `{model_name}`.'
        )
        for param, value_param in params.items():
            display_name = self.get_parameter_display_name(param)
            assert param in model_field.__dict__, (
                f'In the `{field}` attribute of `{model_name}`, '
                f'specify the parameter `{display_name}`.'
            )
            assert model_field.__dict__.get(param) == value_param, (
                f'In the `{field}` attribute of `{model_name}`, '
                f'check whether the value of the `{display_name}` parameter '
                'is the same as in the task.'
            )
