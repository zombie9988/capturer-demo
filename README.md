# capturer-demo

Для компиляции protobuf файлов в класс Python необходимо воспользоваться командой:

```bash
python -m grpc_tools.protoc -I=proto --python_out=. --pyi_out=. --grpc_python_out=. proto/alert.proto
```