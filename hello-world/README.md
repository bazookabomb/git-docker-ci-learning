# virtuelle Umgebung erstellen & aktivieren
python3 -m venv .venv
source .venv/bin/activate

# pip updaten und Abhängigkeiten installieren
python -m pip install --upgrade pip
pip install -r requirements.txt

# Beispiel starten
python hello-world.py
