import httpx
import pytest

@pytest.mark.asyncio
async def test_bybit_api_status():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.bybit.com/v5/market/time")
        assert response.status_code == 200
        assert "retCode" in response.json()
