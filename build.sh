rm -dr dist/

python3 -m eel invoice.py ui --noconsole --onefile

cp -r ui/ dist/ui/
cp database.db dist/database.db
cp -r resources/ dist/resources/