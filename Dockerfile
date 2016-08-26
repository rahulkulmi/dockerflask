FROM ubuntu:14.04
RUN apt-get update && apt-get install -y curl \
 					 vim \
					 python-pip \
					 python-dev \
					 build-essential
COPY run.py .
ADD . /docker
WORKDIR /docker
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
