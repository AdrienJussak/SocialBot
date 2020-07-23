FROM python:3

MAINTAINER adrien.jussak@wascardev.com

COPY . /app
WORKDIR /app

ENV TWITTER_API_KEY ""
ENV TWITTER_API_SECRET ""
ENV TWITTER_USER_KEY ""
ENV TWITTER_USER_SECRET ""
ENV TWITTER_ACCOUNTS ""
ENV DISCORD_WEBHOOK_URL ""

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "socialbot.py"]