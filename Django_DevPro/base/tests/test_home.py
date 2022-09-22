from django.test import Client
from Django_DevPro.django_assertions import assert_contains


def test_status_code(client: Client):
    resposta = client.get('/')
    assert resposta.status_code == 200


def test_title(client: Client):
    resposta = client.get('/')
    assert_contains(resposta, '<title>Python Pro</title>')
