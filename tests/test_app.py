from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_3D.app import app


def test_root_retorna_ok():
    client = TestClient(app)

    resp = client.get('/')

    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {'message': 'Ola'}
