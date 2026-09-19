from __future__ import annotations

import json
import unicodedata
from pathlib import Path

from flask import Flask, abort, render_template, request


BASE_DIR = Path(__file__).resolve().parent


def load_json(filename: str) -> list[dict]:
    with (BASE_DIR / "data" / filename).open(encoding="utf-8") as source:
        return json.load(source)


def normalize(value: str) -> str:
    return "".join(
        char for char in unicodedata.normalize("NFKD", value.casefold())
        if not unicodedata.combining(char)
    )


def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=None)
    if test_config:
        app.config.update(test_config)

    @app.after_request
    def privacy_headers(response):
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.get("/")
    def welcome():
        return render_template("welcome.html", page_title="Informação e apoio", hide_nav=True)

    @app.get("/inicio")
    def home():
        return render_template("home.html", page_title="Início", active="home")

    @app.get("/ajuda-imediata")
    def emergency():
        return render_template("emergency.html", page_title="Ajuda imediata", hide_nav=True)

    @app.get("/apoio")
    def services():
        all_services = load_json("services.json")
        query = request.args.get("q", "").strip()
        category = request.args.get("categoria", "todos").strip().casefold()
        filtered = all_services
        if category != "todos":
            filtered = [item for item in filtered if item["category_slug"] == category]
        if query:
            needle = normalize(query)
            filtered = [
                item for item in filtered
                if needle in normalize(" ".join((item["name"], item["category"], item["neighborhood"], item["summary"])))
            ]
        return render_template(
            "services.html",
            page_title="Rede de apoio",
            services=filtered,
            query=query,
            category=category,
            active="services",
        )

    @app.get("/apoio/<slug>")
    def service_detail(slug: str):
        service = next((item for item in load_json("services.json") if item["slug"] == slug), None)
        if service is None:
            abort(404)
        return render_template("service_detail.html", page_title=service["name"], service=service, hide_nav=True)

    @app.get("/orientacoes")
    def articles():
        return render_template(
            "articles.html",
            page_title="Orientações",
            articles=load_json("articles.json"),
            active="articles",
        )

    @app.get("/orientacoes/<slug>")
    def article_detail(slug: str):
        article = next((item for item in load_json("articles.json") if item["slug"] == slug), None)
        if article is None:
            abort(404)
        return render_template("article_detail.html", page_title=article["title"], article=article, hide_nav=True)

    @app.get("/contato-de-confianca")
    def trusted_contact():
        return render_template("trusted_contact.html", page_title="Contato de confiança", active="contact")

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html", page_title="Página não encontrada", hide_nav=True), 404

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
