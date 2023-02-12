# docker run -it -p 8000:80 app
FROM python:3.10-buster

EXPOSE 8000/tcp

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#CMD docker run -it -p 8000:80 app
