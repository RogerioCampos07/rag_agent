FROM python:3.13-slim


ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


RUN pip install --no-cache-dir poetry


WORKDIR /app


COPY pyproject.toml poetry.lock ./


RUN poetry install --no-root --only main && rm -rf /tmp/poetry_cache

COPY . .


EXPOSE 8501


CMD ["streamlit", "run", "rag_agent/view/page_chat.py", "--server.port=8501", "--server.address=0.0.0.0"]