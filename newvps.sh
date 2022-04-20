#!/bin/bash

export LC_ALL=C
#export LANG=C
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8


# fonts color
red(){
    echo -e "\033[31m\033[01m$1\033[0m"
}
green(){
    echo -e "\033[32m\033[01m$1\033[0m"
}
yellow(){
    echo -e "\033[33m\033[01m$1\033[0m"
}
blue(){
    echo -e "\033[34m\033[01m$1\033[0m"
}
bold(){
    echo -e "\033[1m\033[01m$1\033[0m"
}

mv /etc/localtime /etc/localtime.bak
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

update -y

apt install -y sudo
apt install -y ntp  
apt install -y nano 
apt install -y vim wget git unzip zip tar curl

systemctl enable ntp
systemctl restart ntp

update -y

