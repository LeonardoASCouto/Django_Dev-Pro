import pytest
from django.test import Client
from Django_DevPro.django_assertions import assert_contains
from django.urls import reverse


@pytest.fixture
def resposta(client: Client):
    resposta = client.get(reverse('base:home'))
    return resposta


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_title(resposta):
    assert_contains(resposta, '<title>Python Pro - Home</title>')


def test_home_link(resposta):
    assert_contains(resposta, f'href="{reverse("base:home")}">Python Pro</a>')


def test_home_developer_name(resposta):
    assert_contains(resposta, 'Leonardo Couto')
