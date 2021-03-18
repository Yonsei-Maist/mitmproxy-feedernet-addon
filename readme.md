# MITM Proxy Addon for Feedernet
Read request and response from Feedernet using MITM Proxy  
Can see document of MITM [here](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)  
Can see document of mitmproxy [here](https://mitmproxy.org/)  
Save packet to mysql server (maist.yonsei.ac.kr:3306)

## Environment
pip install list
```
mitmproxy@lastest
python@3.0.0 or more
pymysql@lastest
```
## Install
install of mitmproxy application
```
# install mitmproxy (need root)
# linux
sudo apt install mitmproxy
# macos, windows (need homebrew)
sudo brew install mitmproxy
```
install of project
```
git clone https://github.com/Yonsei-Maist/mitmproxy-feedernet-addon.git
```
## Run
```
# in command line
mitmproxy [options..] -s /path/to/project/MitmproxyFeedernetAddon.py
```
## Author
Chanwoo Gwon, Yonsei Univ. Researcher since 2020.05
## Maintainer
Chanwoo Gwon, arknell@yonsei.ac.kr (2020.09 ~)