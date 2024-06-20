import asyncio
from datetime import datetime
from typing import Optional

import aiohttp
import ccxt.async_support as ccxt
from sqlalchemy.future import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import delete

from app.main.database import get_session
from app.main.database.tables import Currency
from app.main.utils import NotFoundException


async def _save_data_to_db(currency_price: float, currency: str) -> int:

    async with get_session() as db_session:
        currency_obj = Currency(
            currency=currency,
            date_=datetime.now().replace(microsecond=0),
            price=currency_price,
        )
        db_session.add(currency_obj)
        await db_session.commit()
        await db_session.refresh(currency_obj)

    return currency_obj.id


async def _get_price(currency: str, currency_to_bid: str = "USDT"):

    currency_pair_symbol = f"{currency}/{currency_to_bid}"

    try:
        exchange = ccxt.kucoin()

        # Fetch the ticker for the specified currency pair (e.g., 'BTC/USDT')
        ticker = asyncio.create_task(exchange.fetch_ticker(currency_pair_symbol))
        ticker = await ticker
        bid_price = float("%.2f" % ticker["bid"])

        return bid_price

    except ccxt.BadSymbol:
        raise NotFoundException(f"Currency pair '{currency_pair_symbol}' not found")

    finally:
        await exchange.close()


async def get_price_controller(currency: str) -> dict:
    currency_price = await _get_price(currency)
    return await _save_data_to_db(currency_price, currency)

async def get_price_history_controller(page: int) -> dict:
    async with get_session() as db_session:
        price_records = await db_session.execute(select(Currency).offset((page - 1) * 10).limit(10))
        price_records = price_records.scalars().all()

    return [{"currency": record.currency, "price": record.price, "date": record.date_.isoformat()} for record in price_records]

async def delete_price_history_controller() -> None:
    async with get_session() as db_session:
        await db_session.execute(delete(Currency))
        await db_session.commit()