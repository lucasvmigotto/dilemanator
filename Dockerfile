# syntax=docker/dockerfile:1.7-labs

FROM python:3.12-slim as requirements-stage

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /tmp

COPY ./pyproject.toml ./uv.lock /tmp/

RUN uv export \
    --format requirements-txt \
    --output-file /tmp/requirements.txt \
    --no-hashes \
    --no-dev

FROM python:3.12-slim as venv-stage

COPY --from=requirements-stage \
    /tmp/requirements.txt \
    /tmp/

RUN python -m venv /venv

RUN /venv/bin/pip install \
    --upgrade \
    --quiet \
    -r /tmp/requirements.txt

FROM python:3.12-slim as final-stage

WORKDIR /code

COPY --from=venv-stage /venv/ /venv/

ENV PYTHONPATH="${PYTHONPATH}:/code/src/"

ENV APP__HOST='0.0.0.0'
ENV APP__PORT=8080
ENV APP__TOOLBARMODE='viewer'
# ENV APP__DILEMAS_SAMPLES_URL
# ENV APP__MODEL_APIKEY

COPY --parents ./prompts/ ./src/ /code/

EXPOSE ${APP__PORT}

CMD "/venv/bin/python" "-m" \
    "streamlit" "run" "/code/src/app.py" \
    "--server.address" "${APP__HOST}" \
    "--server.port" "${APP__PORT}" \
    "--client.toolbarMode" "${APP__TOOLBARMODE}" \
    "--browser.gatherUsageStats" "False"
