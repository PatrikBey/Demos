*EPM - Demo*: a demonstration for containerized pipelines. 

=========================================================


ABOUT
-----


Plotting of elevated plus maze animal movements.



Container pipeline
----

To use container software please download the udnerlying docker software package 
[https://www.docker.com/products/docker-desktop/]
After installation you can directly start building the example container below.

To build the provided docker container run the following command:

```bash
    docker build . --force-rm  -t epm:latest -f Docker/Dockerfile
```

To run the docker container with test data run the following comannd
```bash
    docker run -v $PWD\\ElevatedPlusMaze\\Data:/data epm:latest
```


