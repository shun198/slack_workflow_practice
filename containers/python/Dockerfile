FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY application/pyproject.toml /code/
# Initialize python project with Poetry
RUN pip install --upgrade pip && pip install poetry
RUN poetry install

