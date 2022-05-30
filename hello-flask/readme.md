## docker build
```shell
export SECRET_A='secret-a'
export SECRET_B='secret-b'
docker build -t hello-flask --build-arg PYTHON_VERSION=3.10 --secret id=a,env=SECRET_A --secret id=b,env=SECRET_B .
```

## docker run
```shell
docker run --rm -p 8000:8000 hello-flask
```
