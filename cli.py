import typer
from rich import print

from bot.orders import (
    place_market_order,
    place_limit_order,
)

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.exceptions import (
    ValidationError,
    BinanceClientError
)

app = typer.Typer()


@app.command()
def trade(
    symbol: str = typer.Option(..., "--symbol"),
    side: str = typer.Option(..., "--side"),
    order_type: str = typer.Option(..., "--order-type"),
    quantity: float = typer.Option(..., "--quantity"),
    price: float = typer.Option(None, "--price"),
    stop_price: float = typer.Option(None, "--stop-price")
):
    """
    Place Binance Futures Testnet orders.
    """

    try:
        side = side.upper()
        order_type = order_type.upper()
        symbol = symbol.upper()

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)
        validate_symbol(symbol)

        print("\n[cyan]Order Request Summary[/cyan]")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )
        elif order_type == "LIMIT":
            response = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

        print("\n[green]Order Placed Successfully[/green]")

        print("\n[yellow]Order Response[/yellow]")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except ValidationError as e:
        print(f"\n[red]Validation Error:[/red] {e}")

    except BinanceClientError as e:
        print(f"\n[red]API Error:[/red] {e}")

    except Exception as e:
        print(f"\n[red]Unexpected Error:[/red] {e}")


if __name__ == "__main__":
    app()