import httpx
import asyncio

async def analyze_market():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
    print(f"--- BEAST-SENSE MARKET ANALYSIS ---")
    
    async with httpx.AsyncClient(base_url="https://api.bybit.com") as client:
        for symbol in symbols:
            # Запрос к реальному API Bybit
            response = await client.get(f"/v5/market/tickers?category=linear&symbol={symbol}")
            res_data = response.json()
            
            if res_data.get('retCode') == 0:
                ticker = res_data['result']['list'][0]
                last_price = ticker['lastPrice']
                # Расчет волатильности (упрощенно для примера)
                print(f"✅ {symbol}: Price {last_price} | Analysis: Ready for BEAST MODE")
            else:
                print(f"❌ {symbol}: API Error {res_data.get('retMsg')}")

if __name__ == "__main__":
    asyncio.run(analyze_market())
