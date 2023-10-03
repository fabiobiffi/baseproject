FROM python:3.10-slim-bullseye

USER root

RUN apt-get update && apt-get install -qq -y \
    wget \
    curl \
    build-essential \
    dnsutils \
    gcc \
    libpq-dev \
    mime-support \
    python3-dev \
    default-libmysqlclient-dev \
    cron \
    systemctl \
    nano \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# enable cron service
RUN systemctl enable cron

WORKDIR /home
RUN mkdir django
RUN mkdir -p django/baseproject
WORKDIR /home/django/baseproject

COPY . .

RUN pip install -r conf/virtualenv/requirements.txt

EXPOSE 8000
CMD ["ci/scripts/entrypoint.sh"]
