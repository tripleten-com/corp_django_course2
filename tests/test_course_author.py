import pytest
from django.urls import reverse


pytestmark = [
    pytest.mark.django_db,
]


def test_superuser_courses(admin_client, courses, courses_with_author):
    expected_count = len(courses) + len(courses_with_author)

    url = reverse('admin:courses_course_changelist')
    response = admin_client.get(url)
    actual_count = response.context_data['cl'].full_result_count

    assert actual_count == expected_count, (
        'Make sure the method `get_queryset` of the admin panel `CourseAdmin` '
        'для суперпользователя возвращаются все курсы.'
    )


def test_author_courses(author_client, courses, courses_with_author):
    expected_count = len(courses_with_author)

    url = reverse('admin:courses_course_changelist')
    response = author_client.get(url)
    actual_count = response.context_data['cl'].full_result_count

    assert actual_count == expected_count, (
        'Make sure the method `get_queryset` of the admin panel `CourseAdmin` '
        'returns only the courses written by an author when they make such a request.'
    )
