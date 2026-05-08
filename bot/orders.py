from binance.exceptions import BinanceAPIException
from bot.client import get_client
from bot.logging_config import logger
from bot.exceptions import (BinanceClientError,
                            parse_binance_error)
import requests
from bot.client import get_symbol_precision
from bot.validators import (
    round_quantity,
    round_price
)
client = get_client()
def place_market_order(
    symbol: str,
    side: str,
    quantity: float
) -> dict:
    try:
        logger.info(
            f"MARKET ORDER | {symbol} | {side} | qty={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Response: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        error_message = str(e)

        if "insufficient balance" in error_message.lower():

            raise BinanceClientError(
               "Insufficient Futures balance."
            )

        elif "margin is insufficient" in error_message.lower():

            raise BinanceClientError(
               "Not enough margin available."
            )

        elif "precision" in error_message.lower():

            raise BinanceClientError(
               "Invalid quantity or price precision."
            )

        elif "invalid symbol" in error_message.lower():

            raise BinanceClientError(
               "Invalid trading symbol."
            )

        else:
           raise BinanceClientError(error_message)
    except requests.exceptions.ConnectionError:

        logger.error("Network connection failed.")

        raise BinanceClientError(
            "Failed to connect to Binance."
        )

    except requests.exceptions.Timeout:

        logger.error("Request timeout.")

        raise BinanceClientError(
            "Binance request timed out"
        )


    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise BinanceClientError(str(e))


def place_limit_order(
    symbol: str,
    side: str,
    quantity: float,
    price: float
) -> dict:
    try:
        precision_info = get_symbol_precision(symbol)

        quantity = round_quantity(
            quantity,
            precision_info["quantity_precision"]
        )

        price = round_price(
            price,
            precision_info["price_precision"]
        )

        logger.info(
            f"LIMIT ORDER | {symbol} | {side} | qty={quantity} | price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Response: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        error_message = str(e)

        if "insufficient balance" in error_message.lower():

            raise BinanceClientError(
               "Insufficient Futures balance."
            )

        elif "margin is insufficient" in error_message.lower():

            raise BinanceClientError(
               "Not enough margin available."
            )

        elif "precision" in error_message.lower():

            raise BinanceClientError(
               "Invalid quantity or price precision."
            )

        elif "invalid symbol" in error_message.lower():

            raise BinanceClientError(
               "Invalid trading symbol."
            )

        else:
           raise BinanceClientError(error_message)
    except requests.exceptions.ConnectionError:

        logger.error("Network connection failed.")

        raise BinanceClientError(
            "Failed to connect to Binance."
        )

    except requests.exceptions.Timeout:

        logger.error("Request timeout.")

        raise BinanceClientError(
            "Binance request timed out"
        )


    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise BinanceClientError(str(e))
