FROM python:3.7-alpine
EXPOSE 80
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]