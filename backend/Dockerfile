FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY requirements.txt .


RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
COPY . .
EXPOSE 8000
