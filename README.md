# app_android

# ВАЖНО!!! В названии папки с main.py не должно быть пробелов. А основной файл должен называться именно main.py
### sudo apt update

### sudo apt upgrade
### sudo apt update
### Вроде как это необязательно, но лучше обновить.

### sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
### pip3 install --user --upgrade Cython==0.29.33 virtualenv 
### export PATH=$PATH:~/.local/bin/
### pip3 install --user --upgrade buildozer

# buildozer init  (ВАЖНО, КОМАНДУ ВВОДИТЬ В ПАПКЕ С MAIN.PY)

### В папке появится файл настроек, редактировать можно как блокнотом так и IDE
### cейчас покажу важные настрйки в файле

# (list) List of inclusions using pattern matching
source.include_patterns = datebase/*,model/*

# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,pymysql,sqlalchemy

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = INTERNET
