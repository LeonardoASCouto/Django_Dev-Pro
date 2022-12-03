import pytest
from Django_DevPro.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy

from Django_DevPro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resposta(client, modulo):
    resposta = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resposta


def test_titulo(resposta, modulo):
    assert_contains(resposta, modulo.titulo)


def test_descricao(resposta, modulo):
    assert_contains(resposta, modulo.descricao)


def test_publico(resposta, modulo):
    assert_contains(resposta, modulo.publico)
