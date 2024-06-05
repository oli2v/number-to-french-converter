PROJECT_NAME=french-converter
IMAGE_NAME=$(PROJECT_NAME)-image
CONTAINER_NAME=$(PROJECT_NAME)-container

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop:
	docker stop $(CONTAINER_NAME)

remove:
	docker rm $(CONTAINER_NAME)