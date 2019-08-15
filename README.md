# MasterWebsiteEcSeg

Web Framework Builit in Django to run ecSeg: Semantic Segmentation of Metaphase Images containing Extrachromosomal DNA.
```
Web Framework: 
Oscar D Sanchez, Jeff Jaureguy
```
## Installation
This platform was built using Python 3.6.7 

To download project dependencies, execute the following commands from a terminal: 

```
git clone https://github.com/Jaure020/MasterWebsiteEcSeg.git
pip3 install -r requirements.txt
```
## Run ecSeg Web Framework
To generate the website, run from terminal:
```
python3 manage.py runserver
```
## For OperationalError: no such table: auth_user
To load table correctly
```
python3 manage.py migrate --run-syncdb
```
