import pytest


@pytest.mark.asyncio
async def test_hello(client):
    client = await client
    resp = await client.get("/price")

    # Perform assertions on `resp` to validate the test
    assert resp.status == 200
    assert await resp.json() == {"message": "Price is 1000"}
    assert await resp.text() == '{"message": "Price is 1000"}'
