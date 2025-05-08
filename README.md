# NoSINT 
[NoSINT](https://nosint.org) API wrapper available on Arch, Debian, Android with Termux and iOS with iSH Shell. 

![Image](https://github.com/user-attachments/assets/8dc14107-9b0a-4fea-bcab-69638480f44e)

## ⚠️ Before Installing ⚠️
You will first need to [Register](https://nosint.org/auth/register) at nosint.org and acquire your API token from  [Dashboard](https://nosint.org/auth/register)

## 🛠️ Install 🛠️

[![Arch Linux](https://img.shields.io/badge/Arch%20Linux-%230C8BDC?style=for-the-badge&logo=arch-linux&logoColor=white)](#)

[![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)](#)

[![Debian](https://img.shields.io/badge/Debian-A81D33?style=for-the-badge&logo=debian&logoColor=fff)](#)


### [![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=apple&logoColor=white)](#) 
 iSH:
- Install dependencies: 
```
apk add git bash python3 py3-pip py3-colorama
```
- Install tool: 
```
cd $HOME
git clone https://github.com/cons0le7/nosint.git
chmod +x $HOME/nosint/nosint $HOME/nosint/update.sh $HOME/nosint/update_2.sh 
ln -s $HOME/nosint/nosint /usr/bin/nosint
nosint
```
### Termux: 
- Install dependencies: 
```
apt-get install git python3 pip
pip install colorama
```
- Install tool: 
```
cd $HOME
git clone https://github.com/cons0le7/nosint.git
chmod +x $HOME/nosint/nosint $HOME/nosint/update.sh $HOME/nosint/update_2.sh 
ln -s $HOME/nosint/nosint /data/data/com.termux/files/usr/bin/nosint
nosint
```
### Debian: 
- Install dependencies: 
```
sudo apt-get update
sudo apt-get install git python3 python3-pip
pip3 install colorama
```
- Install tool: 
```
cd ~
git clone https://github.com/cons0le7/nosint.git
chmod +x ~/nosint/nosint ~/nosint/update.sh ~/nosint/update_2.sh
sudo ln -s ~/nosint/nosint /usr/local/bin/nosint
sudo nosint
```
### Arch: 
- Install dependencies: 
```
sudo pacman -Sy git python python-pip
pip3 install colorama
```
- Install tool: 
```
cd ~
git clone https://github.com/cons0le7/nosint.git
chmod +x ~/nosint/nosint ~/nosint/update.sh ~/nosint/update_2.sh
sudo ln -s ~/nosint/nosint /usr/bin/nosint
sudo nosint
```
