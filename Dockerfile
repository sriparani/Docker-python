FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
EXPOSE 80
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
