import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


def get_client() -> Client:
    """
    Create Binance Futures Testnet client.
    """

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    return client


client = get_client()


def get_symbol_precision(symbol: str) -> dict:
    """
    Fetch Binance Futures symbol precision.
    """

    exchange_info = client.futures_exchange_info()

    for s in exchange_info["symbols"]:

        if s["symbol"] == symbol:

            return {
                "quantity_precision": s["quantityPrecision"],
                "price_precision": s["pricePrecision"]
            }

    return {}