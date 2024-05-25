build:
	docker build -t transcription:1.0 .

run:
	docker run --rm -v $(pwd):/app -it transcription:1.0 python transcription.py