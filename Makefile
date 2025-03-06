frontendimagename := frontend
backendimagename := backend

docker-compose: docker-compose-clean
	@docker-compose build
	@docker-compose up -d 
	@docker ps -a
	@docker-compose ps

docker-compose-clean:
	@docker-compose down