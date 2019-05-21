FROM python:3.7.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install uWSGI

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN python {{ project_name }}/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["uwsgi", "--ini", uwsgi.ini"]
