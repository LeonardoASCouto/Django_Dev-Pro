import pytest
from django.urls import reverse

from model_mommy import mommy
from Django_DevPro.aperitivos.models import Video
from Django_DevPro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + 'video_nao_existente',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_video_title(resp, video):
    assert_contains(resp, f'>{video.titulo}</h')


def test_video_content(resp, video):
    assert_contains(resp,
                    f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}?h=ddccff4790&amp;badge=0&amp'
                    f';autopause=0'
                    f'&amp;player_id=0&amp;app_id=58479"')
