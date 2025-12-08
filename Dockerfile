FROM python:3.13-slim

#Install uv
RUN pip install uv

WORKDIR /app

#copy project files.
COPY pyproject.toml .
COPY main.py .
COPY .env .

#install dependencies using uv

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

