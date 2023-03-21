# FROM ubuntu:18.04

# RUN mkdir -p /src
# COPY Code /src

# WORKDIR /src

# RUN apt-get -qq update && \
#     apt-get -yq install git&& \
#     apt-get -yq install python3-pip

# RUN pip3 install openMINDS

FROM python:3.8-slim-buster
MAINTAINER Patrik Bey <patrik.bey@bih-charite.de>

RUN mkdir -p /openminds/src
COPY Code /openminds/src

WORKDIR /openminds

COPY /Docker/requirements.txt /openminds/requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get -qq update && \
    apt-get install -yq git
ENV GIT_PYTHON_REFRESH=quiet


RUN python3 -c 'import openMINDS,openMINDS.version_manager ; openMINDS.version_manager.init()'

