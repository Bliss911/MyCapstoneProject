FROM python:3.7-alpine

COPY . /app

WORKDIR /app


RUN python -m pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9000

CMD ["python3", "app.py"]
