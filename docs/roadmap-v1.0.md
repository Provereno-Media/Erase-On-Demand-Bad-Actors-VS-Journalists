# Roadmap: публикация v1.0.0

**Дедлайн публикации:** 2026-10-03 (сб)  
**Составлено:** 2026-09-27, по состоянию репозитория на коммите `5fbd277`

## 0. Выявленные расхождения (блокеры релиза)

| # | Проблема | Факт в репозитории |
|---|---|---|
| B1 | Число кейсов | `cases.csv` = 33 строки; CHANGELOG = 32; audit/README = 35 |
| B2 | Число источников | `sources.csv` = 36; CHANGELOG = 29 |
| B3 | Сравнительные кейсы | `comparative_cases.csv` = 5; CHANGELOG = 7 |
| B4 | Версия | `datapackage.json` = 1.1.0; CHANGELOG = [1.0.0] от 2026-09-25 (до релиза) |
| B5 | Достоверность | 32 Confirmed + 1 Unverified (AIPLEX-001) — тексты не должны утверждать «все Confirmed» |
| B6 | PENDING-источники | SRC-031, SRC-032, SRC-035 без архивных ссылок |
| B7 | Нет валидации | отсутствуют `scripts/` и `.github/workflows` |

## 1. Пн 28.09 — Инвентаризация и заморозка скоупа
- [x] Сверить список case_id с audit и case-notes; решить судьбу 2 «пропавших» кейсов (добавить или исправить audit) — B1
- [ ] Зафиксировать скоуп v1.0: всё, что не закрывается до 01.10, помечается как known limitation, а не блокер
- [ ] Завести GitHub milestone `v1.0.0` и issues по пунктам B1–B7

## 2. Вт 29.09 — Доказательная база (приоритеты из audit)
- [ ] SRC-031/032/035: снять и архивировать Meta-уведомления (archive.org / archive.today + локальная копия в Vault), вписать URL
- [ ] Архивировать снимки Google TR (Reporter ID 40866 и др.) — волатильные данные
- [ ] MON-001, RESP-001, GAYLAN-001: попытка получить второй источник; если нет — оставить, отметить в limitations
- [ ] AIPLEX-001: оставить Unverified, явно указать в README

## 3. Ср 30.09 — Корпоративный OSINT (best effort)
- [ ] Ares Rights (BORME), Initiatrix, Bytescare (MCA), Mogul Press (штат США)
- [ ] Связь MarkScan ↔ AiPlex (MCA / LinkedIn)
- [ ] Что не найдено — `registration_status = not_obtained` + дата проверки

## 4. Чт 01.10 — Целостность данных и tooling (feature freeze)
- [x] `scripts/validate.py`: `frictionless validate data/datapackage.json`, проверка FK (source_ids, actor_ids), контролируемых словарей по codebook
- [x] `.github/workflows/validate.yml` — CI на push/PR
- [ ] Унифицировать `last_verified`, дубли и пустые обязательные поля
- [ ] Проверка case-notes: по одной на кейс/кластер, ссылки на SRC-ID корректны

## 5. Пт 02.10 — Документация, этика, безопасность
- [ ] Пересчитать все цифры в README, CHANGELOG, audit, methodology (B1–B5)
- [x] `datapackage.json` version → 1.0.0 (или обосновать 1.1.0 и переименовать релиз)
- [ ] PII-ревью: скриншоты `case-notes/shishkin-like/`, WhatsApp-переписка, имена физлиц (Ripu/Aditya Singh, Dhorelia) — формулировки без юридических обвинений, только уровень достоверности
- [ ] Проверить, что VAULT-материалы не попали в публичный репо (`git log --all -- <paths>`)
- [x] Добавить `CITATION.cff`; подготовить Zenodo-интеграцию для DOI
- [x] Раздел Known limitations в README
- [ ] Финальный вычитки RU/EN терминологии (trusted flagger и др.)

## 6. Сб 03.10 — Релиз
- [ ] Финальный прогон валидации, CHANGELOG `[1.0.0] - 2026-10-03`
- [ ] Тег `v1.0.0`, GitHub Release с notes и архивом данных
- [ ] DOI через Zenodo; ссылка в README
- [ ] Анонс: EFCSN, партнёры (Qurium, OCCRP), пострадавшие редакции — предупредить заранее

## Post-v1.0 (v1.1)
- Второй источник для MON-001 / GAYLAN-001 / RESP-001
- Анализ DSA VLOP-отчётов Facebook/Instagram (август 2026) и Google PDF
- Policy brief для EC DSA enforcement unit / IMCO
