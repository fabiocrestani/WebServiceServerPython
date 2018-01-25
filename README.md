Aplicação base de Web Service REST escrito em Python
===

* Instalar as ferramentas do python:
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

* Setar um ambiente
```
sudo apt-get install python3-venv
mkdir environments
cd environments
python3 -m venv my_env
source my_env/bin/activate
```

* Instalar o Flask
```
pip install Flask
```

* Rodar o servidor
```
./run.sh
```

