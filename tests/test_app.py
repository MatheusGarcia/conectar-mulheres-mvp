from app import create_app


def client():
    return create_app({"TESTING": True}).test_client()


def test_public_pages_load_without_login():
    web = client()
    for path in ("/", "/inicio", "/ajuda-imediata", "/apoio", "/orientacoes", "/contato-de-confianca"):
        assert web.get(path).status_code == 200


def test_service_search_uses_python_filter():
    response = client().get("/apoio?q=ednalva")
    assert response.status_code == 200
    assert "Centro de Referência Ednalva Bezerra" in response.get_data(as_text=True)
    assert "DEAM João Pessoa" not in response.get_data(as_text=True)


def test_unknown_detail_returns_404():
    assert client().get("/apoio/inexistente").status_code == 404


def test_privacy_headers_are_present():
    response = client().get("/inicio")
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert response.headers["Cache-Control"] == "no-store"
