import pytest
from django.urls import reverse
from Django_DevPro.django_assertions import assert_contains

from model_mommy import mommy
from Django_DevPro.aperitivos.models import Video


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_video_title(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_video_link(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{video_link}"')
#
#
# def test_video_content(resp):
#     assert_contains(resp,
#                     '<iframe src="https://player.vimeo.com/video/760589226?h=ddccff4790&amp;badge=0&amp;autopause=0'
#                     '&amp;player_id=0&amp;app_id=58479"')
