
FROM python:3.9.13-alpine3.15
WORKDIR /miapp3
COPY miapp3/ /miapp3
RUN pip install -r /miapp3/conf.d/requeriments.txt
CMD ["python3", "/python:3.9.13-alpine3.15/app.py"]