from aiohttp import web

from app.main.router.price import get_price_handler, get_price_history_handler, delete_price_history_handler


def create_app():
    app = web.Application()
    app.router.add_get("/price/{currency}", get_price_handler)
    app.router.add_get("/price/history/", get_price_history_handler)
    app.router.add_delete("/price/history/", delete_price_history_handler)
    return app
