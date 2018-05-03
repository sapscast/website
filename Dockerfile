FROM python:3.6-alpine

RUN apk add --update tini

ADD . /

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["gunicorn", "--bind", "0.0.0.0:80", "website.__main__:app"]
