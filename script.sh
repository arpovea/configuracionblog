#! /usr/bin/bash 
#Activamos el entorno virtual
source bin/activate
#Guardo cambios en el repositorio de configuración:
git add .
git commit -am "Agregando y modificando informacion"
git push

#Genero el sitio:
pelican content -s pelicanconf.py
#Desactivamos el entorno virtual
deactivate
#Me cambio al repositorio en el que esta el blog y aplico cambios:
cd ../blog-web/
git add .
git commit -am "Agregando y modificando informacion"
git push
cd -
