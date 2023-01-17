FROM ubuntu:18.04

RUN mkdir -p /src
COPY Code /src

WORKDIR /src

RUN apt-get -qq update && \
    apt-get -yq install git&& \
    apt-get -yq install python3-pip

RUN pip3 install openMINDS

