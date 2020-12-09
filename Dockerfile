FROM python:3.8-alpine

WORKDIR /app
ENV FLASK_RUN_PORT=9443
ENV FLASK_APP=app.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9443
COPY . .
CMD ["flask", "run", "--host=0.0.0.0"]
