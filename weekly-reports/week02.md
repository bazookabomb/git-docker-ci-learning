  1 # Woche 02 - Python Umgebung Learnig Log

  ## Lernziel

  ---

  - Python-Umgebung (`venv`), `requirements.txt`, `pip`
  - Editor/IDE (VS Code) + Extensions, Linter (`flake8`), Formatter (`black`)
  - Testen mit pytest
  - hooks in pre-commit
  - Projekt-Setup + README + `.gitignore`

  ## Inhalte

  ---
  - Pythonumgebung reproduzierbar (pip freeze > requirements.txt) erstellen
  - Extensions z.B. Prettier in VS Code und flake8 und black per pip install
  - Testen mit Testfunktionen und pytest
  - vor jedem Commit soll flake8, black, pytest laufen
  - Dokumentation der Installschritte in der README, eine gitignore anlegen

  ## Praxis

  ---

  - siehe Inhalte

  ## Erkenntnisse

  ---

  - Die Extensions erleichtern VS Code
  - flake8 und black erzeugen sauberen, einheitlich formatierten Quellcode
  - pytest ermgöglicht schnelle Tests
  - pre-commit automatisiert alles oben genanntes vor dem commit
  - eine gute README und gitignore sind wichtig

  ## Probleme

  ---

  - die rev-Angabe in der pre-commit yaml zunächst nicht verstanden aber es ermöglicht reproduzierbare Entwicklungsumgebungen und kann mit pre-commit autoupdate auf den aktuellsten Stand gebracht werden

  ## Nächste Schritte

  ---

  - Docker wiederholen und festigen
