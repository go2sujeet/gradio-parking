say_hello:
	echo "Hello, World!"

run_local:
	python src/main.py

build_docker_image:
	docker build -t my-gradio-parking . --no-cache

run_docker_image:
	docker-compose up

build_and_run_docker_image:
	$(MAKE) build_docker_image
	$(MAKE) run_docker_image
	
publish_docker_image:
	docker-compose build publish2hub
	docker push go2sujeet/my-gradio-parking:latest



