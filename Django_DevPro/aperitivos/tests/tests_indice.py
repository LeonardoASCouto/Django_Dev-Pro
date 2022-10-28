import pytest
from django.urls import reverse
from Django_DevPro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'title',
    [
        'Vídeo Aperitivo: Motivação',
        'Vídeo Aperitivo: Instalação'
    ]
)
def test_video_title(resp, title):
    assert_contains(resp, title)
#
#
# def test_video_content(resp):
#     assert_contains(resp,
#                     '<iframe src="https://player.vimeo.com/video/760589226?h=ddccff4790&amp;badge=0&amp;autopause=0'
#                     '&amp;player_id=0&amp;app_id=58479"')
