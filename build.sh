python -m venv .venv

.venv/bin/activate

pip install -r requirements.txt

playwright install

python discord_bot.py