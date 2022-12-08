import pytest
from Django_DevPro.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy

from Django_DevPro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resposta(client, aula):
    resposta = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resposta


def test_titulo(resposta, aula):
    assert_contains(resposta, aula.titulo)


def test_vimeo_id(resposta, aula):
    assert_contains(resposta, f'src="https://player.vimeo.com/video/{aula.vimeo_id}')
