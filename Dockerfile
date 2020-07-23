FROM python:3

MAINTAINER adrien.jussak@wascarde.com

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "socialbot.py"]