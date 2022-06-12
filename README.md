#Metasploit Payload Generation

##using kali linux


* Update and upgrade your machine
```bash
$ apt update && apt upgrade
```
* Clone project
```bash
$ git clone https://github.com/WIZARD00007/MSFpayloadGenerator
```
* Installing requirements
```bash
$ cd MSFpayloadGenerator
$ chmod +x setup.py
$ python3 setup.py 
```
* Generating Payload
```bash
$cd src
$ chmod +x payload.py
$ python3 payload.py
```
##using termux

Intsalling metasploit framework
``` bash
$ pkg install wget
$ wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh
$ chmod +x metasploit.sh
```

* Update and upgrade your machine
```bash
$ pkg install git
$ pkg update && pkg upgrade
```
* Clone project
```bash
$ git clone https://github.com/WIZARD00007/MSFpayloadGenerator
```
* Installing requirements
```bash
$ cd MSFpayloadGenerator
$ chmod +x setup.py
$ python3 setup.py 
```
* Generating Payload
```bash
$cd src
$ chmod +x payload.py
$ python3 payload.py
