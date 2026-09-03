# checkout-pricing

Небольшой внутренний сервис расчёта цены для корзины.

- `app/pricing.py` — считает итоговую цену строки заказа (`calculate_final_price`).
- `app/discounts.py` — применяет плоскую скидку к итогу перед оплатой (`apply_discount`).
- `app/api.py` — точка входа `checkout()`, связывает расчёт цены и применение скидки.
- `tests/test_pricing.py` — тесты на `app/pricing.py`.

Запуск тестов из корня `sandbox/`:

```
python -m pytest
```
