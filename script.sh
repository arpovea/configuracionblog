#! /usr/bin/bash 

#Guardo cambios en el repositorio de configuración:
git add .
git commit -am "Agregando y modificando informacion"
git push

#Genero el sitio:
pelican content -s pelicanconf.py

#Me cambio al repositorio en el que esta el blog y aplico cambios:
cd ../blog-web/
git add .
git commit -am "Agregando y modificando informacion"
git push
