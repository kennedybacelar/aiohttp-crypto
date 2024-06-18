from aiohttp import web

from app.main.router.price import get_price


def create_app():
    app = web.Application()
    app.router.add_get("/price", get_price)
    return app
