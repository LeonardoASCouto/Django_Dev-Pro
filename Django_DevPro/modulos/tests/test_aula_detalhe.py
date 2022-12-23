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
def resp_com_usuario_logado(client_com_usuario_logado, aula):
    return client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))


def test_titulo(resp_com_usuario_logado, aula):
    assert_contains(resp_com_usuario_logado, aula.titulo)


def test_vimeo_id(resp_com_usuario_logado, aula):
    assert_contains(resp_com_usuario_logado, f'src="https://player.vimeo.com/video/{aula.vimeo_id}')


def test_modulo_breadcrumb(resp_com_usuario_logado, modulo: Modulo):
    assert_contains(resp_com_usuario_logado,
                    f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


@pytest.fixture
def resp_sem_usuario(client, aula):
    return client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))


def test_usuario_nao_logado_redirect(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))
