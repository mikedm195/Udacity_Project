FROM python:3.7.3-stretch

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    make=4.1-9.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64
RUN chmod +x /bin/hadolint

RUN pip3 install -r /app/requirements.txt 
#&& rm -rf /root/.cache

CMD [ "python3", "main.py" ]
