FROM python:3.12.4-slim-bookworm

WORKDIR /app

# install python dependency
RUN pip install --upgrade pip && pip install poetry==1.8.3
COPY ./app/poetry.lock ./poetry.lock
COPY ./app/pyproject.toml ./pyproject.toml
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi\
    && pip cache purge

COPY ./app /app