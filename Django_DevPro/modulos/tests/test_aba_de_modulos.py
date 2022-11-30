import pytest
from django.test import Client
from Django_DevPro.django_assertions import assert_contains
from django.urls import reverse
from model_mommy import mommy

from Django_DevPro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resposta(client, modulos):
    resposta = client.get(reverse('base:home'))
    return resposta


def test_home_developer_name(resposta, modulos):
    for modulo in modulos:
        assert_contains(resposta, modulo.titulo)
