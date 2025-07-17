run:
	docker-compose run --rm app sh -c "python manage.py runserver"

dockerUp:
	docker-compose up

dockerBuild:
	docker-compose build

migrate:
	docker-compose run --rm app sh -c "python manage.py makemigrations"
	docker-compose run --rm app sh -c "python manage.py migrate"

createsuperuser:
	docker-compose run --rm app sh -c "python manage.py createsuperuser"

shell:
	python manage.py shell

test:
	docker-compose run --rm app sh -c "python manage.py test"

collectstatic:
	python manage.py collectstatic --noinput

lint:
	flake8 .

resetdb:
	rm db.sqlite3
	python manage.py migrate
	python manage.py createsuperuser

waitdbAndMigrate:
	docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
