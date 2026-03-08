FROM debian:stable-slim

RUN apt update && apt upgrade && apt install python3 -y

COPY main.py main.py
COPY books/ books/
# RUN ["sudo", "apt", "install", "python"]
CMD ["python3", "main.py"]