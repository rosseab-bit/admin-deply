
FROM python:3.9.13-alpine3.15
WORKDIR /miapp2
COPY miapp2/ /miapp2
RUN pip install -r /miapp2/conf.d/requeriments.txt
CMD ["python3", "/python:3.9.13-alpine3.15/app.py"]