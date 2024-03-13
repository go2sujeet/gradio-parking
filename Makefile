say_hello:
	echo "Hello, World!"
run_local:
	python src/main.py
build_docker_image:
	docker build -t my-gradio-parking . --no-cache
run_docker_image:
	docker run -p 8080:8080 my-gradio-parking
