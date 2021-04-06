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
RUN nohup mitmweb 2>&1 & echo $! > process
RUN kill `cat process`

## cp pem file to crt
RUN mkdir /usr/share/ca-certificates/mitm
RUN cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/share/ca-certificates/mitm/
WORKDIR /usr/share/ca-certificates/mitm/
RUN openssl x509 -in ./mitmproxy-ca-cert.pem -inform PEM -out ./mitmproxy-ca-cert.crt

## register crt file in Ubuntu
RUN dpkg-reconfigure ca-certficates
RUN update-ca-certificates

# start server
ENTRYPOINT ["mitmweb"]
CMD ["-m reverse:https://localhost:443 -p 9443 --web-port 8443 -s MitmproxyFeedernetAddon.py"]