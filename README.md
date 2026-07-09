# Lernplan: Entwicklungs- und Containertechnologien

## Ziel

- **Kurz:** Sicherer Umgang mit Git, reproduzierbaren Entwicklungsumgebungen, Docker/Compose, grundlegender CI und ein kleines containerisiertes Abschlussprojekt.
- **Zielgruppe:** Einsteiger bis Fortgeschrittene, die strukturierte Praxis mit Container‑Workflows und CI wünschen.

## Dauer & Tempo

- **Empfohlen:** 6–8 Wochen (8 Wochen für entspanntes Tempo).
- **Tägliche Zeit:** 6–8 Stunden, aufgeteilt in Theorie, Praxis und Review.

## Wochenübersicht

- **Woche 1 — Git & Versionsverwaltung:** Konzepte, Branch‑Workflows, Remote (GitHub), Pull Requests, Übungen.
- **Woche 2 — Entwicklungsumgebungen & Tools:** `venv`, `requirements.txt`, VS Code, Linter (`flake8`), Formatter (`black`), Debugging.
- **Woche 3 — Docker Grundlagen:** Images, Container Lifecycle, `Dockerfile`, Volumes, Ports.
- **Woche 4 — Multi‑Container & Compose:** `docker-compose`, Netzwerke, Multi‑Stage Builds, Registry (Push/Pull).
- **Woche 5 — Grundlagen Automatisierung (CI):** CI‑Konzepte, GitHub Actions, Tests in CI, automatisches Linting.
- **Woche 6 — Tests & Dokumentation:** `pytest`, Test‑Reports, dokumentierbare Dev‑Setups, Reproduzierbarkeit.
- **Woche 7 — Abschlussprojekt:** Planen, Implementieren, Testen, CI konfigurieren, Image pushen.
- **Woche 8 — Puffer & Vertiefung:** Fehlerbehebung, Performance, weiterführende Themen.

## Wöchentliche Checkpoints

- **Ende Woche 1:** PR + Merge abgeschlossen
- **Ende Woche 3:** Lokales Docker‑Image lauffähig
- **Ende Woche 5:** CI‑Workflow führt Tests & Build aus
- **Ende Woche 7:** Abschlussprojekt im Repo + gepushte Images

## Lernmethoden & Empfehlungen

- **Active Recall:** Am Ende jeder Sitzung 5 Fragen beantworten
- **Feynman‑Methode:** Kurze schriftliche Erklärungen verfassen
- **Kleine Ziele:** Tasks in 30–60 min‑Blöcke teilen
- **Cheat‑Sheets:** z. B. `git-cheatsheet.md`, `docker-cheatsheet.md`

## Praktische Artefakte / Deliverables

- **Repo‑Struktur:** Quellcode, `Dockerfile`, `docker-compose.yml`, `requirements.txt`, `README.md`
- **CI:** `.github/workflows/ci.yml` mit Tests + Build
- **Dokumentation:** Setup‑Schritte, Troubleshooting, Usage


