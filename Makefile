say_hello:
	echo "Hello, World!"
run_local:
	python src/main.py
build_docker_image:
	docker build -t my-gradio-parking . --no-cache
publish_docker_image:
	docker-compose build publish2hub
	docker push go2sujeet/my-gradio-parking:latest

run_docker_image:
	docker-compose up

