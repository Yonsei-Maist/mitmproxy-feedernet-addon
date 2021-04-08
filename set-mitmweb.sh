#!/bin/bash

nohup mitmweb 2>&1 & echo $! > process
FILE=./process
if [ -f "$FILE" ]
then
  kill `cat "$FILE"`

  ## cp pem file to crt
  mkdir /usr/share/ca-certificates/mitm
  cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/share/ca-certificates/mitm/
  cd /usr/share/ca-certificates/mitm/
  openssl x509 -in ./mitmproxy-ca-cert.pem -inform PEM -out ./mitmproxy-ca-cert.crt

  ## register crt file in Ubuntu
  dpkg-reconfigure ca-certficates
  update-ca-certificates
fi