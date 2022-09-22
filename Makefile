run:
	FLASK_APP=app.py flask run

debug:
	FLASK_APP=app.py flask --debug run

all: debug
