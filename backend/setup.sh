docker-compose -f dev-docker-compose.yml build
docker-compose -f dev-docker-compose.yml run homework-backend python manage.py migrate
docker-compose -f dev-docker-compose.yml run homework-backend python manage.py create_schedules
docker-compose -f dev-docker-compose.yml up
