FROM python:3.13-slim

#Install uv
RUN pip install uv

WORKDIR /app

#copy project files.
COPY . .

#install dependencies using uv

RUN uv sync

EXPOSE 8001

CMD ["uv", "run", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8001"]

