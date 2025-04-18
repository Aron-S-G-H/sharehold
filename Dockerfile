FROM python:3.13.3-slim

WORKDIR /source

COPY . /source/

RUN apt-get update -y && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    apt-transport-https \
    unixodbc \
    unixodbc-dev \
    libodbc1 \
    odbcinst \
    odbcinst1debian2 \
    && curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && echo "deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean

RUN pip install pip --upgrade && \
    pip install -r requirements.txt

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=off

RUN chmod +x /source/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/source/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]