---
title: Cambio de Arquitectura
author: Adrián Rodríguez Povea
status: draft
Summary: Buenas! En esta ocasión se va a realizar el cambio de una arquitectura x86_64 (amd64) a la arquitectura i386

---

Buenas! En esta ocasión se va a realizar el cambio de una arquitectura x86_64 (amd64) a una arquitectura i386 por completo, se va a utilizar una máquina con un sistema Debian Buster(amd64).

***


## Cambio de Arquitectura (De amd64 a i386):

#### Paso 1: Agregar arquitectura i386.

Para ello utiliza:

```
sudo dpkg --add-architecture i386
```

Luego actualizamos la lista de paquetes:

```
sudo apt-get update
```

#### Paso 2: Guardar lista de paquetes instalados en el sistema amd64.

A continuacíon se creará un fichero con los nombres de todos los paquetes del sistema con la arquitectura "amd64":

```
dpkg -l | grep '^.i' | awk '{print $2}' | grep :amd64 | tr '\n' ' ' > paquetesamd64.txt
```

Como se puede ver se excluye aquellos que tienen que ver con el kernel, puesto que estos se instalarán a mano.

Una vez realizado esto, se crea otro fichero donde se almacenan los nombres de estos mismos paquetes pero cambiando :amd64 por :i386 (la arquitectura).

```
dpkg -l | grep '^.i' | awk '{print $2}' | grep :amd64 | egrep -v 'linux-image-.*' | sed 's/:amd64/:i386/g' | tr '\n' ' ' > paquetesi386.txt
```

#### Paso 3: Instalación de paquetes

Se han realizado los ficheros con la lista de paquetes para descargar estos paquetes con "apt" y instalar con "dpkg", ya que "apt" al instalar paquetes de una arquitectura borra el de la anterior arquitectura, lo que provoca que el sistema se rompa.

Los paquetes descargados se almacenan en "/var/cache/apt/archives/" por lo que interesa tener este directorio limpio, para ello:

```
sudo apt-get clean
```

Una vez limpio el directorio, realiza la descarga los paquetes de los distintos instaladores en su version i386:


```
sudo apt-get -y --no-install-recommends --download-only install dpkg:i386 apt:i386 aptitude:i386 apt-utils:i386
```

Luego instalalos con:

```
sudo dpkg --install /var/cache/apt/archives/*.deb
sudo dpkg --install /var/cache/apt/archives/dpkg_*.deb
```

Si da problemas al procesar recuerda intentarlo de nuevo la instalación, si da problemas de configuración realiza: `sudo dpkg --configure -a`


Una vez instalados estos dara problemas de dependencias para arreglar esto utiliza:

```
sudo apt --fix-broken -y --allow-remove-essential
```

Una vez realizado descarga todos los paquetes del fichero paquetesi386.txt:

```
cat paquetesi386.txt | sudo xargs apt-get -y --no-install-recommends --download-only install
```

Ahora instala las librerias y perl:

```
sudo dpkg --install /var/cache/apt/archives/lib*.deb /var/cache/apt/archives/perl*.deb
```

Luego instala los demas:

```
sudo dpkg --install /var/cache/apt/archives/*.deb
```

### Borrado de paquetes amd64

Realizamos los siguiente:

```
sudo apt-get autoremove
```