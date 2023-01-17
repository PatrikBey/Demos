FROM python:3.8-slim-buster

RUN mkdir -p /src
COPY Code /src
ENV Hello=World
WORKDIR /src

RUN pip3 install -r requirements.txt

RUN pip3 install progressbar2

CMD [ "python", "/src/RUN.py"]
