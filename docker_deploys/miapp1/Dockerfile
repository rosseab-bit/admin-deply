
FROM python:3.9.13-alpine3.15
WORKDIR /miapp1
COPY miapp1/ /miapp1
RUN pip install -r /miapp1/conf.d/requeriments.txt
CMD ["python3", "/python:3.9.13-alpine3.15/app.py"]