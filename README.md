# Reasoning Harness — когнитивная оболочка (манифест)
*Рабочее имя проекта: «Думающий Клод».*

**Статус:** собрано и провалидировано независимым оценщиком (2026-06-28). 16 скиллов (2 — `prioritization`, `benchmark` — в кладбище после релиза-вычитания). Упаковано в плагин `reasoning-harness` для установки в Cowork и Claude Code.

Слой управления контекстом поверх Claude: ядро-методология (всегда активна) + 16 скиллов-режимов (по необходимости) + память. Не отдельная модель, а reasoning harness. Доменно-независима: работает для бизнеса, стратегии, инвестиций, контента и разработки.

## Структура

```
thinking-claude/
├── CLAUDE.md                   # ЯДРО: принципы + роутер + фазы + гейты (ставится как инструкции)
├── portable-system-prompt.md   # 1-страничная версия для любого чата
├── README.md                   # этот манифест
├── .claude-plugin/
│   └── marketplace.json        # маркетплейс для установки плагина
├── reasoning-harness/          # ПЛАГИН (то, что устанавливается)
│   ├── .claude-plugin/plugin.json
│   ├── skills/                 # 16 модулей-режимов
│   ├── commands/test-module.md # /test-module — A/B-проверка модулей
│   └── README.md
├── memory/
│   ├── PROJECT-MEMORY.md        # долговечный контекст и решения
│   └── HYPOTHESIS-LEDGER.md     # реестр гипотез + все вердикты тестов
└── _build/                      # DEV-инструменты (не для повседневной работы)
    ├── ROLLOUT.md
    ├── EVALUATOR-PROMPT.md       # промпт независимого оценщика
    └── CONFIRMING-TESTS.md
```

Историческая версия архитектуры (до релиза-вычитания 2026-06-28, 18 скиллов) — `_build/Архитектура_blueprint_OLD.md`. Актуальный источник — `ARCHITECTURE.md` в корне.

## Где и насколько работает

| Среда | Полнота | Что нужно поставить |
|---|---|---|
| **Cowork** | полная (с плагином) | Ядро → Инструкции проекта; плагин `reasoning-harness` → через Customize → Plugins |
| **Claude Code** | полная | `CLAUDE.md` в корень репо; плагин или скиллы в `.claude/skills/` |
| **Claude chat** | ядро | вставить `CLAUDE.md` в инструкции claude.ai-проекта или `portable-system-prompt.md` первым сообщением. Память тут не нужна |

## Развёртывание

**Cowork (полноценно):**
1. Содержимое `CLAUDE.md` → правая панель проекта → Instructions. **Только в одно место** (project Instructions ИЛИ глобальные user preferences, не оба сразу) — иначе ядро грузится в контекст по нескольку раз за сессию (см. `INSTALL-COWORK.md`).
2. Плагин: Customize (левая панель) → вкладка Plugins → Personal → «+» → **Add marketplace** → указать папку `thinking-claude` (или её git-репозиторий) → установить **reasoning-harness**. После этого 16 скиллов и `/test-module` доступны по «/».

**Claude Code:**
1. `CLAUDE.md` → в корень репозитория.
2. `/plugin marketplace add <путь к папке thinking-claude>` → `/plugin install reasoning-harness@thinking-claude`. (Либо вручную: `reasoning-harness/skills/*` → `.claude/skills/`, `reasoning-harness/commands/*` → `.claude/commands/`.)

**Claude chat:** создать проект на claude.ai, вставить `CLAUDE.md` в его инструкции (или `portable-system-prompt.md` первым сообщением). Скиллы там не автозагружаются — при нужде вставляешь содержимое нужного скилла вручную.

## Итог валидации (16 KEEP, 2 в кладбище)

Сильнейшие: `fact-mode`, `verification`, `discovery`, `adjacent-fields`, `pre-mortem`, `divergent`, `roles`, `alternatives`. С суженными триггерами: `benchmark`, `amplifier` (keep), `prioritization` (условный keep). Сквозной урок: модуль ценен там, где **ловит то, что база упускает**, а не дублирует её — поэтому триггеры узкие. Детали — в `memory/HYPOTHESIS-LEDGER.md`.

## Обслуживание (режим эксплуатации)

- **Активная оценка (наблюдатель)** — always-on в ядре: ловит под-роутинг и упущения по ходу работы (заменил еженедельный Overseer, v1.3.0).
- **Реестр гипотез** — копит решения; гипотезы стареют в факты или отсеиваются.
- **Тестирование новых правок** — `/test-module` + независимый о