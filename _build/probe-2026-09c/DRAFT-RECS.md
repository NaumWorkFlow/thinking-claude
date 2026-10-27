# Черновик: что убрать / переписать в Reasoning Harness под Opus 5.5 (основная) и Fable 5.1 (вторая)

Объект: `/home/claude/tc/CLAUDE.md` (ядро, 163 строки), `/home/claude/tc/reasoning-harness/` (16 скиллов, 4 команды), `/home/claude/tc/memory/`.
Данные проб: `RESULTS.md` рядом с этим файлом. Сырые ответы исполнителей: `../out/pNN.md`, ключ: `KEY.md`.

## Первоисточники (цитаты из документации Anthropic, собраны 27.09.2026)
- Prompting Claude Opus 5 (действует и для 5.5 как преемника): «If your prompt contains explicit verification instructions ("include a final verification step for any non-trivial task," "use a subagent to verify"), remove them: instructions like these cause over-verification on Claude Opus 5 … The same applies to legacy harness scaffolding that adds separate verification steps.» · «Avoid instructing re-checks it already performs ("double-check your answer," "re-verify before responding")». · «Do not delegate work you can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check your own work.» · «Claude Opus 5 can also expand the scope of a task … For narrow tasks, constrain scope explicitly».
- Prompting Claude Opus 5.5: убрать «think carefully» / «think step by step» / просьбы писать рассуждение в ответе: «The model decides for itself how much to think, and effort is the main control»; просьбы воспроизвести внутреннее рассуждение в тексте ответа могут отклоняться категорией `reasoning_extraction`. Строки вида «Answer directly without deliberating» — «measure quality … because less thinking can lower it». Дефолтный effort у Opus 5.5 — `medium` (у Opus 5 был `high`).
- What's new in Opus 5.5: «much less likely than recent models to take hard-to-reverse actions»; «more likely to ask the user before taking a potentially destructive action».
- System card Opus 5.5: «the top subcategory of flagged behavior was asserting unverified inferences as established fact»; «more likely than previous models to follow malicious instructions in text that a user pastes into their own prompt»; «less self-preference bias than Claude Mythos 5.1 across most measures».
- Prompting Claude Fable 5.1: рекомендованный Anthropic блок «Keep changes to what the request needs. Something else you notice worth doing … a change to a file the task didn't require — is a suggestion to make at the end, not a change to make»; Fable 5.1 «delivers what's asked for and sometimes more: it may fix nearby code»; на low effort реже ищет и чаще отвечает по памяти (дан готовый «verification nudge» про имена из быстро меняющихся областей); анти-форматные правила старых моделей теперь подавляют нужную структуру.

## 0. Главное — не содержание, а доставка
В текущей среде (приложение Claude, облачная сессия со связанной папкой) ядро НЕ загружается: в контекст попадает только корневой `CLAUDE.md`-указатель (2,9 КБ), строка `@thinking-claude/CLAUDE.md` не разворачивается (в сессию выгружается один файл без папки), инструкции проекта claude.ai пусты, инструкций Cowork в контексте нет. Подтверждено двумя субагентами (Opus 5.5 и Fable 5.1) и листингом `/mnt/user-data/uploads/cowork-folders/…/` (там один файл). Здесь харнес = только плагин; ссылки скиллов на «принцип 10/19» висят в пустоте.
→ Рекомендация: выбрать носитель для этой среды (инструкции проекта claude.ai «Создание думающих ИИ…» или сам корневой CLAUDE.md папки с полным текстом) и пересмотреть правило «один носитель = указатель» — в этой среде указатель не работает. Проверить, грузится ли ядро в десктопном Cowork, открыв там сессию и спросив про принцип 10.

## 1. Убрать (устарело или противоречит рекомендациям производителя)
1.1 Принцип 13, вторая половина («Больше шагов рассуждения ≠ лучше: используй минимум … длинный reasoning плодит лишние гипотезы»). Мышление всегда включено и управляется effort; такие строки у Opus 5.5 могут снижать качество. Оставить только «минимально достаточный контекст».
1.2 Таблица в «Роутере» (5 строк) — полный дубль таблицы наблюдателя (9 строк), грузится в каждый запрос.
1.3 Принцип 16 (обратимость) — дубль принципа 10.
1.4 В «Поведении по умолчанию» строка про мета-чек на развилках — дубль принципа 12.
1.5 Принцип 18 и строка «Выражайся простым языком» в «Коммуникации» — слить в одну.
1.6 `fact-mode` п.2 «Chain-of-Verification: сгенерируй проверочные вопросы к своему ответу и ответь на них» — это ровно «double-check your answer», который производитель велит убрать. Заменить на узкое правило: имя/цифра из быстро меняющейся области → искать, даже если «помнишь» (формулировка Anthropic для Fable 5.1).
1.7 `prompt-builder`: из списка техник убрать *Chain-of-thought* («рассуждения по шагам») и *Self-consistency* для промптов под Opus 5.5 / Fable 5.1; вместо этого — строка «рекомендуй уровень effort». Просьба писать рассуждения в ответе может дать отказ `reasoning_extraction` на Opus 5.5.
1.8 `_build/probe-2026-09b/` (неотслеживаемый стенд под opus-5, не запускался) — в архив/удалить: модель-адресат заменена, а сам кейс прогнан сейчас на новых моделях (T10: 0/16 молчаливых расширений).

## 2. Переписать
2.1 Форсаж, п.3 «Обязательны, даже если пограничны: red-team, verification, независимый проход» → verification = только исполнимые проверки (прогон, grep, открыть ссылку); red-team — по сигналу; независимый проход — только для само-оценочных решений (keep/drop, оценка своей работы), а не для каждой форсажной задачи. Плюс: «глубина по максимуму» → явно «подними effort (high/xhigh/max), если доступно». Основание — цитаты производителя; Форсаж пробами НЕ проверялся.
2.2 Фаза 6 «итерируй 4–6 … максимум 2 цикла» — оставить стоп-правило, но убрать формулировку, требующую отдельного цикла верификации там, где есть исполнимая проверка.
2.3 `orchestrator`, таблица «блок → модель»: сейчас Opus 4.8 / Sonnet 5 / Fable 5 / Haiku 4.5. Новая: основная работа, архитектура, планирование → Opus 5.5; самое сложное и независимый суд → Fable 5.1 (другая модель, чем писавшая — это и есть принцип 19); объёмная рутина → Sonnet 5; мелочь → Haiku 4.5.
2.4 `memory/PROJECT-MEMORY.md`: «Claude Code работает на Sonnet 4.6», аксиома H8 «Sonnet для рутины из-за цены» — основание (цена Opus) изменилось: Opus 5.5 $4/$20 против $5/$25 у Opus 5; пересмотреть, а не переносить.
2.5 `verification`, регламент независимого прохода: явно сузить до keep/drop и оценки своей работы; добавить «не для рутинной перепроверки» (цитата производителя про субагентов).
2.6 `/harness-probe`: ловушку 10 заменить конструкцией T9 (дефект в соседнем файле портит результат, который требует DoD) — это первая проба, где фон в контроле ненулевой (BASE правил чужой файл 5/6). Ловушки 6–8 (арифметика, agent theater, молчаливый гейт) — кандидаты на удаление как малоинформативные.
2.7 `ARCHITECTURE.md` §5.1, `HYPOTHESIS-LEDGER.md`: новая эпоха `opus-5.5 / fable-5.1`; записать probe-2026-09c.

## 3. Оставить (с основаниями)
3.1 Принципы 1–2, 17 (не выдумывай, метки знания) — главный класс ошибок Opus 5.5 по system card; T1: без ядра Opus 5.5 дал неверный DOI 2/2, с ядром 0/2.
3.2 Принцип 10 целиком, включая «по шагу, а не по задаче» — T9: без ядра обе модели правили не заказанный файл (fx.py) 5/6 и README 5/6, с ядром 0/6 и 1/6; тот же принцип Anthropic сам рекомендует для Fable 5.1. (T10 разницы не дал: 0/16 везде.)
3.3 Принцип 20 — пробы: 12/12 устояли и в BASE, но system card фиксирует регресс именно по вставленному тексту; строка дешёвая.
3.4 Принцип 3, раздел «Коммуникация» — предпочтения пользователя, не компенсация слабости модели.
3.5 Принципы 9, 11, 14, анти-паттерны, порог субагентов (Фаза 0 п.3) — совпадают с рекомендациями производителя.
3.6 Принцип 12 в суженной форме — совпадает с рекомендациями производителя; T9 не показал over-verification от ядра.
3.7 `fact-mode`: search-first и «цитата только из открытого источника» — оставить (Fable 5.1 на low effort реже ищет).

## 4. Кандидаты, которые нельзя решить без замера (принцип 19, судья — человек)
4.1 Таблица сигналов наблюдателя дублирует триггеры в `description` скиллов (переписаны в 1.4.0, H21: 32/32). Возможно, наблюдатель можно сжать до правила градации — нужен замер маршрутизации без таблицы.
4.2 Очередь ре-базлайна скиллов: `steelman` (фактически шаг 1 `red-team`) — сильнейший кандидат на слияние; далее `divergent`, `alternatives`, `roles`, `amplifier`. Пробами этой сессии не проверялись.
