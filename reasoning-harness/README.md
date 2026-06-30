# Reasoning Harness — плагин «Думающий Клод»

Когнитивная оболочка: 18 скиллов-режимов, которые подключаются по необходимости и дисциплинируют мышление над сложными задачами (бизнес, стратегия, инвестиции, разработка, контент).

## Скиллы (18)
architect · prompt-builder · roles · red-team · adjacent-fields · landscape · benchmark · alternatives · divergent · memory · verification · pre-mortem · steelman · prioritization · fact-mode · amplifier · discovery · overseer

## Команда
`/test-module <имя>` — A/B-проверка модуля (нужен ли он, не вредит ли).

## Установка
Этот каталог — плагин внутри маркетплейса `thinking-claude` (`../.claude-plugin/marketplace.json`).
- **Cowork:** Customize → Plugins → Personal → «+» → Add marketplace → указать папку `thinking-claude` (или её git-репозиторий) → установить плагин **reasoning-harness**.
- **Claude Code:** `/plugin marketplace add <путь-к-папке-thinking-claude>` → `/plugin install reasoning-harness@thinking-claude`.

## Важно
Это только скиллы. «Ядро» методологии (всегда-активные принципы) — в `../CLAUDE.md`, его ставят как инструкции проекта (Cowork) или в корень репозитория (Claude Code). Память и реестр гипотез — в `../memory/`.
