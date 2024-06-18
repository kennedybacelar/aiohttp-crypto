from aiohttp import web

from app.main.controller.price import get_price_controller


async def get_price(request):
    data = await get_price_controller("kennedybacelar")
    return web.json_response(data)
