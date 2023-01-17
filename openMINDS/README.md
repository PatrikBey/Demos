*openMINDS - Demo*: a demonstration for containerized pipelines. 

=========================================================


ABOUT
-----


creating an interactive container for openMINDS



Container pipeline
----

To use container software please download the udnerlying docker software package 
[https://www.docker.com/products/docker-desktop/]
After installation you can directly start building the example container below.

To build the provided docker container run the following command:

```bash
    docker build . --force-rm  -t openminds:latest -f Docker/Dockerfile
```

To run the docker container with test data run the following comannd
```bash
    docker run -it -v $PWD\\openMINDS\\Data:/data openminds:latest bash
```


