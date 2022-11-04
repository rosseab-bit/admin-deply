
FROM python:3.9.13-alpine3.15
WORKDIR /miapp5
COPY miapp5/ /miapp5
RUN pip install -r /miapp5/conf.d/requeriments.txt
CMD ["python3", "/miapp5/app.py"]