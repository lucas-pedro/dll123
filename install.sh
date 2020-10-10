#!/bin/bash



#instalação do pip
sudo apt install python3-pip > logs.txt

#instalação das dependencias

sudo pip3 install PySimpleGUI 

printf "\e[1;77mRequerimentos Instalados\n\e[0m"
