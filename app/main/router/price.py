from aiohttp import web
import json

from app.main.controller.price import get_price_controller, get_price_history_controller, delete_price_history_controller


async def get_price_handler(request):
    currency = request.match_info.get("currency")
    saved_currency_id = await get_price_controller(currency)
    data = {"currency_id": saved_currency_id}
    return web.json_response(data)

async def get_price_history_handler(request):
    page = request.query.get('page', 1)
    data = await get_price_history_controller(page)
    return web.json_response(data)

async def delete_price_history_handler(request):
    await delete_price_history_controller()
    return web.json_response({"message": "Price history deleted"})