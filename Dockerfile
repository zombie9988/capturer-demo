FROM python:3.10

COPY ./ /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I=proto --python_out=. --pyi_out=. --grpc_python_out=. proto/alert.proto
EXPOSE 50051

CMD [ "python3", "app.py"]