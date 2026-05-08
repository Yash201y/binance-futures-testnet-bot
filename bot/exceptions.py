class ValidationError(Exception):
    """
    Raised for invalid user input.
    """
    pass


class BinanceClientError(Exception):
    """
    Raised for Binance/API related errors.
    """
    pass


def parse_binance_error(error) -> str:
    """
    Convert Binance API errors into
    user-friendly messages.
    """

    message = str(error).lower()

    if "precision" in message:
        return "Invalid quantity or price precision."

    if "insufficient balance" in message:
        return "Insufficient Futures balance."

    if "margin is insufficient" in message:
        return "Not enough margin available."

    if "invalid symbol" in message:
        return "Invalid trading symbol."

    if "timeout" in message:
        return "Binance request timed out."

    return str(error)