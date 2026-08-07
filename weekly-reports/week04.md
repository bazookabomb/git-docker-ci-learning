# Woche 04 - Docker Compose

## Lernziel

  - Tag 1–2: `docker-compose` Grundlagen, Services, Netzwerke.
  - Tag 3–4: Multi‑Stage Builds, Umgebungsvarianten (dev/prod).
  - Tag 5: Registry (Docker Hub) push/pull, Image-Tagging.
  - Tag 6–7: Übung: kleine App mit DB via Compose.

---

## Inhalte

  - flask und redis compose app erstellt nach Anleitung der öffentlichen Docker Compose docs
    - compose yaml erweitert um die Datenbank zuerst zu starten
    - develop.watch hinzugefügt
  - multi stage build in der Dockerfile
  - deployn Videos zu Docker und Compose geschaut
  - Theorie: tagging und push und pull DockerHub
  - viele Compose yamls gelesen
  - Flask-Postgres-Compose App selber erstellt

---

## Praxis

  siehe Inhalte

---

## Erkenntnisse

  - multi stage builds in der dockerfile (z.B. dev und prod) können in der compose.yaml explizit angefordert werden
  - compose yamls lesen ist einfacher als sie selbst zu schreiben aber Erweiterungen und IntelliSense in VSCode erleichtern es

---

## Probleme

---

## Nächste Schritte

  - Grundlagen Automatisierung (CI)
