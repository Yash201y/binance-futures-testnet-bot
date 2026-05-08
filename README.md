# Binance Futures Testnet Trading Bot

A Python-based CLI trading bot for Binance USDT-M Futures Testnet.

This application allows users to place MARKET, LIMIT, and STOP_MARKET orders on Binance Futures Testnet with proper validation, structured logging, and exception handling.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- Place STOP_MARKET orders
- Supports BUY and SELL sides
- CLI-based interface using Typer
- Input validation
- Structured logging
- API error handling
- Network failure handling
- Binance Futures Testnet support
- Clean modular project structure

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── exceptions.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── cli.py
├── requirements.txt
└── README.md