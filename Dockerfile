FROM python:3-alpine
LABEL maintainer="FejkFejkov25"
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "main.py" ]
