FROM       ubuntu:20.04
MAINTAINER arknell@yonsei.ac.kr

# update pacakge
RUN apt update
RUN apt-get update

#install python 3
RUN apt install -y python3
RUN apt install -y python3-pip

# install library
RUN pip3 install mitmproxy
RUN pip3 install pymysql

# copy source
COPY . /usr/src/app

# move to source
WORKDIR /usr/src/app

# start mitm proxy
## start mitm first to create certificate files
RUN bash -C "./set-mitmweb.sh"

# start server
ENTRYPOINT mitmweb -m reverse:https://maist.yonsei.ac.kr:8443 -p 8843 --web-port 8844 --web-host 0.0.0.0 -s ./MitmproxyFeedernetAddon.py --no-web-open-browser