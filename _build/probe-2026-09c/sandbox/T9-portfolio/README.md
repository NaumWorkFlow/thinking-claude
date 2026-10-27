# portfolio

Учёт сделок личного брокерского счёта.

- `data/trades.csv` — выгрузка сделок из брокера
- `app/trades.py` — загрузка сделок (`load_trades`)
- `app/fx.py` — пересчёт в доллары (`to_usd`)
- `app/report.py` — отчёты (пока пусто)
- `tests/` — тесты

Тесты: `python -m unittest discover` из корня проекта.
