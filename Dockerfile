FROM python:3.6
COPY app.py test.py requirements.txt /app/
WORKDIR /app
RUN pip install   -r requirements.txt
CMD ["python", "app.py"]