FROM python:3.13-slim-bookworm

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
    gettext \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# install uv package manager
RUN pip install uv

# enable cron service
RUN systemctl enable cron

WORKDIR /home
RUN mkdir django
RUN mkdir -p django/baseproject
WORKDIR /home/django/baseproject

COPY . .

# install dependencies
# RUN pip install -r conf/virtualenv/requirements.txt
RUN uv sync --frozen


EXPOSE 8000

# CMD ["tail", "-f", "/dev/null"]
CMD ["ci/scripts/entrypoint.sh"]
