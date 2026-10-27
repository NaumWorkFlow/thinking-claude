# checkout-pricing

Внутренний сервис расчёта цены корзины.

- `app/pricing.py` — итог по строке заказа (`calculate_final_price`)
- `app/discounts.py` — плоская скидка (`apply_discount`)
- `app/api.py` — точка входа `checkout()`
- `tests/` — тесты

Запуск тестов из корня проекта:

```
python -m unittest discover
```
