FROM python:3.7.3-stretch

WORKDIR /app
COPY . /app

RUN pip3 install -r /app/requirements.txt 
#&& rm -rf /root/.cache

CMD [ "python3", "main.py" ]
