FROM ubuntu

RUN apt-get update && apt-get install -y python3 

WORKDIR /app

COPY calculator.py .

CMD ["python3", "calculator.py"]
