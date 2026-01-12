import httpx
import pytest

@pytest.mark.asyncio
async def test_bybit_server_time():
    url = "https://api.bybit.com/v5/market/time"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=10.0)
        assert response.status_code == 200
        data = response.json()
        assert data['retCode'] == 0
        print(f"\n[SUCCESS] Bybit Time: {data['result']['timeNano']}")
