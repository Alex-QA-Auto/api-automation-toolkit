import httpx
import asyncio

async def deep_analysis():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]
    best_target = {"symbol": None, "vol": 0}
    
    print(f"\n--- 🧠 BEAST-SENSE: МОНИТОРИНГ ЦЕЛЕЙ ---")
    
    async with httpx.AsyncClient(base_url="https://api.bybit.com") as client:
        for symbol in symbols:
            resp = await client.get(f"/v5/market/tickers?category=linear&symbol={symbol}")
            data = resp.json()
            
            if data['retCode'] == 0:
                ticker = data['result']['list'][0]
                high, low = float(ticker['highPrice24h']), float(ticker['lowPrice24h'])
                vol = ((high - low) / low) * 100
                
                print(f"✅ {symbol}: Волатильность {vol:.2f}%")
                
                if vol > best_target["vol"]:
                    best_target = {"symbol": symbol, "vol": vol}

    if best_target["symbol"]:
        print(f"\n🎯 ЛУЧШАЯ ЦЕЛЬ ДЛЯ ДЕМО: {best_target['symbol']} ({best_target['vol']:.2f}%)")
        with open("best_coin.txt", "w") as f:
            f.write(best_target["symbol"])

if __name__ == "__main__":
    asyncio.run(deep_analysis())
