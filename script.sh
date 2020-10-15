#! /usr/bin/bash 

#Guardo cambios en el repositorio de configuración:

git add.
git commit -am "Agregando y modificando informacion"
git push
pelican content -s pelicanconf.py
cd ../blog-web/
git add .
git commit -am "Agregando y modificando informacion"
git push
