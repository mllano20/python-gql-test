FROM python:3.9

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib \
    && apt-get install sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD [ "uvicorn", "server:app" ]
