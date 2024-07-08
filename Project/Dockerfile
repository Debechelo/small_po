## Build
FROM python:latest AS build

ARG PYTHONUNBUFFERED
ARG PYTHONIOENCODING

ENV PYTHONUNBUFFERED=${PYTHONUNBUFFERED} \
    PYTHONIOENCODING=${PYTHONIOENCODING}

COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh
 

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]