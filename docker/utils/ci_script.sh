#!/bin/bash

docker-compose exec -u alcali web pip install --quiet --user -r requirements/test.txt
while ! [[ $(docker-compose exec -u alcali web alcali check | grep -P "db:\tok") ]]; do
  echo "Waiting Database..."
  docker-compose exec -u alcali web alcali check
  sleep 10
done
docker-compose exec -u alcali web alcali migrate
docker-compose exec -u alcali web alcali shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').count() or User.objects.create_superuser('admin', 'admin@example.com', 'password')"

while ! [[ $(docker-compose logs | grep "The Salt Master has cached the public key for this node") ]]; do
  echo "Waiting Salt Master..."
  sleep 10
done
docker-compose exec -u alcali web pytest
