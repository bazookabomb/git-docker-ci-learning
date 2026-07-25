# Docker Cheat Sheet — Kurzreferenz

Dieses Cheat Sheet enthält die wichtigsten Docker-Befehle kompakt und nach Themen geordnet.

## Grundlagen
- **Docker Version:** `docker --version`
- **Daemon & Systeminfo:** `docker info`
- **Login (Registry):** `docker login`
- **System aufräumen (vorsichtig):** `docker system prune -a --volumes`

## Images
- **Lokale Images auflisten:** `docker images` oder `docker image ls`
- **Image ziehen:** `docker pull <image>[:tag]`
- **Image bauen:** `docker build -t <name>:<tag> .`
- **Image taggen:** `docker tag <local> <repo>/<name>:<tag>`
- **Image pushen:** `docker push <repo>/<name>:<tag>`
- **Image löschen:** `docker rmi <image>`

## Container
- **Einmalig interaktiv:** `docker run -it --rm <image> <cmd>`
- **Im Hintergrund (Daemon):** `docker run -d -p <host_port>:<container_port> -v <host>:<container> -e KEY=VAL --name <name> <image>`
- **Laufende Container:** `docker ps`
- **Alle Container (auch gestoppte):** `docker ps -a`
- **Stop / Start / Restart:** `docker stop <id|name>` / `docker start <id|name>` / `docker restart <id|name>`
- **Container löschen:** `docker rm <id|name>`
- **Logs (live):** `docker logs -f <container>`
- **Befehl in laufendem Container ausführen:** `docker exec -it <container> /bin/bash` oder `/bin/sh`
- **Dateien kopieren (Host <-> Container):** `docker cp <src> <dest>`
- **Details anzeigen:** `docker inspect <container>`
- **Ressourcen-Metriken in Echtzeit:** `docker stats`

## Netzwerk & Volumes
- **Netzwerke anzeigen:** `docker network ls`
- **Netzwerk erstellen:** `docker network create <name>`
- **Volumes anzeigen:** `docker volume ls`
- **Volume erstellen:** `docker volume create <name>`
- **Volume entfernen:** `docker volume rm <name>`

## Speichern / Laden von Images
- **Image exportieren (tar):** `docker save -o <file.tar> <image>`
- **Image importieren:** `docker load -i <file.tar>`

## Docker Compose (v2 `docker compose`)
- **Services starten (im Vordergrund):** `docker compose up`
- **Services im Hintergrund starten:** `docker compose up -d`
- **Stoppen & entfernen:** `docker compose down`
- **Logs aller Services:** `docker compose logs -f`
- **Compose-Images bauen:** `docker compose build`

## Nützliche Kurzbefehle & Troubleshooting
- **Platz schaffen:** `docker system prune` (oder mit `-a --volumes` für radikaleres Aufräumen)
- **Container-IP schnell sehen:** `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>`
- **Security-Scan:** `docker scan <image>`
- **Einfach debuggen:** `docker run --rm -it --entrypoint sh <image>`
- **Schnell alle gestoppten Container entfernen:** `docker container prune`
- **Schnell alle ungennutzten Images entfernen:** `docker image prune -a`

## Kurzbeispiele
- Einfacher Webserver im Hintergrund (Port-Forwarding & Name):

```bash
docker run -d -p 8080:80 --name webserver nginx:latest
```

- Interaktive Shell in einem laufenden Container:

```bash
docker exec -it webserver /bin/bash
```

- Compose starten (im Hintergrund):

```bash
docker compose up -d
```

## Quick Reference (häufig gebraucht)
- Starten: `docker run`
- Stoppen: `docker stop`
- Logs: `docker logs`
- Interaktiv: `docker exec -it`
- Build: `docker build`
- Compose: `docker compose up`

---
