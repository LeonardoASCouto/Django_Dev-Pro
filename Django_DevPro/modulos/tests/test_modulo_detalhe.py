import pytest
from Django_DevPro.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy

from Django_DevPro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resposta(client, modulo, aulas):
    resposta = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resposta


def test_titulo(resposta, modulo):
    assert_contains(resposta, modulo.titulo)


def test_descricao(resposta, modulo):
    assert_contains(resposta, modulo.descricao)


def test_publico(resposta, modulo):
    assert_contains(resposta, modulo.publico)


def test_aulas_titulo(resposta, aulas):
    for aula in aulas:
        assert_contains(resposta, aula.titulo)
