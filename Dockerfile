FROM python:3.10-slim

WORKDIR /app

ARG MACHINE
ENV MACHINE=${MACHINE}

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]