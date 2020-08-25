FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /hackpy
WORKDIR /hackpy
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . /hackpy/