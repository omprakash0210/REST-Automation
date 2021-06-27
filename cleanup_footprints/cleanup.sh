sudo docker rmi -f $(sudo docker stop $(sudo docker ps -a -q --filter ancestor=omprakash4pt/rest-auto:v11))
sudo docker system prune -f -a
