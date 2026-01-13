import httpx
import asyncio
import logging
import os

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("beast_sense.log"),
        logging.StreamHandler()
    ]
)

async def analyze_market():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]
    best_target = {"symbol": None, "vol": 0}
    
    logging.info("--- 🧠 BEAST-SENSE: START DEEP ANALYSIS ---")
    
    async with httpx.AsyncClient(base_url="https://api.bybit.com", timeout=10.0) as client:
        for symbol in symbols:
            try:
                resp = await client.get(f"/v5/market/tickers?category=linear&symbol={symbol}")
                data = resp.json()
                
                if data.get('retCode') == 0:
                    ticker = data['result']['list'][0]
                    high, low = float(ticker['highPrice24h']), float(ticker['lowPrice24h'])
                    vol = ((high - low) / low) * 100
                    
                    logging.info(f"✅ {symbol}: Волатильность {vol:.2f}%")
                    
                    if vol > best_target["vol"]:
                        best_target = {"symbol": symbol, "vol": vol}
                else:
                    logging.error(f"Ошибка API для {symbol}: {data.get('retMsg')}")
            except Exception as e:
                logging.error(f"Сбой при запросе {symbol}: {e}")

    if best_target["symbol"]:
        logging.info(f"🎯 ЛУЧШАЯ ЦЕЛЬ ДЛЯ ДЕМО: {best_target['symbol']} ({best_target['vol']:.2f}%)")
        with open("best_coin.txt", "w") as f:
            f.write(best_target["symbol"])

if __name__ == "__main__":
    asyncio.run(analyze_market())
