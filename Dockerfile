FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /hackpy
WORKDIR /hackpy
COPY requirements.txt 
RUN pip install -r requirements.txt
COPY . /hackpy/