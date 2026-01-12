import httpx
import pytest

@pytest.mark.asyncio
async def test_simple_ping():
    # Просто пингуем публичный API, без сложностей
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.bybit.com/v5/market/time")
        assert response.status_code == 200
        print(f"Server is alive!")
