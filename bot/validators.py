from bot.exceptions import ValidationError
from bot.client import get_client
client = get_client()
VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_side(side: str)-> None:
    """
    Validate BUY/SELL order side.
    """
    if side.upper() not in VALID_SIDES:
        raise ValidationError(
            f"Invalid side: {side}. Use BUY or SELL."
        )


def validate_order_type(order_type: str)-> None:
    """
    Validate supported order type.
    """
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValidationError(
            f"Invalid order type: {order_type}"
            f"Allowed values: "
            f"MARKET, LIMIT, STOP_MARKET."
        )


def validate_quantity(quantity: float)-> None:
    """
    Validate order quantity.
    """
    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than 0."
        )


def validate_price(price, order_type)-> None:
    """
    Validate LIMIT order price.
    """
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValidationError(
                "LIMIT orders require a valid price."
            )

def validate_symbol(symbol: str)-> None:
    """
    Validating about trading symbol exists
    on Binance Futures Testnet.
    """
    exchange_info = client.futures_exchange_info()

    valid_symbols = {
        s["symbol"]
        for s in exchange_info["symbols"]
    }

    if symbol.upper() not in valid_symbols:
        raise ValidationError(
            f"Invalid symbol: {symbol}"
        )
            
def round_quantity(quantity, precision)-> None:
    """
    Round quantity according to
    Binance symbol precision.
    """
    return round(quantity, precision)


def round_price(price, precision)->None:
    """
    Round price according to
    Binance symbol precision.
    """
    return round(price, precision)