# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# ENV APP__DILEMAS_SAMPLE
ARG USERNAME="vscode"

ENV VIRTUAL_ENV="/home/${USERNAME}/.venv"
ENV UV_PROJECT_ENVIRONMENT="/home/${USERNAME}/.venv"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

USER ${USERNAME}

WORKDIR /code

ENV PYTHONPATH="${PYTHONPATH}:/code/src"
