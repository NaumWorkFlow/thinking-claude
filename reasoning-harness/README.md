# Reasoning Harness — плагин «Думающий Клод»

Когнитивная оболочка: 16 скиллов-режимов, которые подключаются по необходимости и дисциплинируют мышление над сложными задачами (бизнес, стратегия, инвестиции, разработка, контент).

## Скиллы (16)
architect · prompt-builder · roles · red-team · adjacent-fields · landscape · alternatives · divergent · memory · verification · pre-mortem · steelman · fact-mode · amplifier · discovery · overseer

(`benchmark` и `prioritization` — в кладбище `../_build/graveyard/`, не входят в плагин.)

## Команды
- `/test-module <имя>` — A/B-проверка модуля (нужен ли он, не вредит ли).
- `/harness-probe` — регресс-пробы после смены модели (канонические ловушки).

## Установка
Этот каталог — плагин внутри маркетплейса `thinking-claude` (`../.claude-plugin/marketplace.json`).
- **Cowork:** Customize → Plugins → Personal → «+» → Add marketplace → указать папку `thinking-claude` (или её git-репозиторий) → установить плагин **reasoning-harness**.
- **Claude Code:** `/plugin marketplace add <путь-к-папке-thinking-claude>` → `/plugin install reasoning-harness@thinking-claude`.

## Важно
Это только скиллы. «Ядро» методологии (всегда-активные принципы) — в `../CLAUDE.md`, его ставят как инструкции проекта (Cowork) или в корень репозитория (Claude Code). Память и реестр гипотез — в `../memory/`.
