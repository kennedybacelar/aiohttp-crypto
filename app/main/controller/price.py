from typing import Optional

import aiohttp
from sqlalchemy.future import select

from app.main.database import get_session
from app.main.database.tables import Users


async def _select_data_from_table() -> Optional[list]:

    async with get_session() as db_session:
        q = select(Users).offset(0).limit(10)
        result = await db_session.execute(q)
        curr = result.scalars().all()

        for i in curr:
            print(i)

    return None


async def get_price_controller(user: str):

    user = "kennedybacelar"

    url_price = f"https://api.github.com/users/{user}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url_price) as resp:
            user_data = await resp.json()

    result = await _select_data_from_table()
    return result

    return user_data
