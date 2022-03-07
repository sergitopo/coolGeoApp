FROM python:3.8-alpine3.14

WORKDIR /server

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /server/requirements.txt
RUN pip install -r requirements.txt
COPY . /server

CMD ["python", "app.py"]