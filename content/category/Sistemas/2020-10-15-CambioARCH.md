---
title: Cambio de Arquitectura
author: Adrián Rodríguez Povea
status: published
Summary: Buenas! En esta ocasión se va a realizar el cambio de una arquitectura amd64 a una arquitectura i386

---

Buenas! En esta ocasión se va a realizar el cambio de una arquitectura amd64 a una arquitectura i386 por completo, se va a utilizar una máquina con un sistema Debian Buster(amd64).

***

## Cambio de Arquitectura (De amd64 a i386):

Lo primero que se va a realizar es una actualización de todos los paquetes de nuestro equipo a su última versión estable, para ello,

```
sudo apt-get update && sudo apt-get upgrade -y
```

### Agregar arquitectura i386.

Para ello utiliza:

```
sudo dpkg --add-architecture i386
```

Luego actualiza la lista de paquetes:

```
sudo apt-get update
```

### Instalación de paquetes

Se van a descargar estos paquetes con "apt" y instalar con "dpkg", ya que "apt" al instalar paquetes de una arquitectura borra el de la anterior arquitectura, lo que provoca que el sistema se rompa.

Los paquetes descargados se almacenan en "/var/cache/apt/archives/" por lo que interesa tener este directorio limpio, para ello:

```
sudo apt-get clean
```

Una vez limpio el directorio, realiza la descarga los paquetes de los distintos instaladores en su versión i386 esto provocará el cambio de arquitectura principal:

```
sudo apt-get -y --no-install-recommends --download-only install dpkg:i386 apt:i386 aptitude:i386 apt-utils:i386
```

Luego instálalos con:

```
sudo dpkg --install /var/cache/apt/archives/*.deb
```

Si da problemas al procesar recuerda intentar de nuevo la instalación, si da problemas de configuración realiza: `sudo dpkg --configure -a`


Una vez instalados estos dara problemas de dependencias, para arreglar esto utiliza:

```
sudo apt-get --fix-broken install -y --allow-remove-essential
```

A continuación descarga todos los paquetes amd64 pero con la versión i386, menos el kernel:

```
sudo apt-get --download-only -y --no-install-recommends install `dpkg -l | grep '^.i' | awk '{print $2}' | grep :amd64 | egrep -v 'linux-image-.*' | sed 's/:amd64/:i386/g'`
```

Ahora instala las librerías y perl (esto suele reducir los errores):

```
sudo dpkg --install /var/cache/apt/archives/lib*.deb /var/cache/apt/archives/perl*.deb
```

Realiza el siguiente comando para asegurar que no hay ningún paquete sin configurar: 

```
sudo dpkg --configure -a
```

Instala los demás paquetes:

```
sudo dpkg --install /var/cache/apt/archives/*.deb
```

Recuerda realizar de nuevo la instalación si algún paquete da error, sobre todo de dependencias.

***

### Borrado de paquetes amd64 y instalacion del kernel i386

Una vez instalados todos los paquetes de la arquitectura i386, solo queda borrar los paquetes de amd64 y instalar el kernel i386.

Realiza el siguiente comando para borrar los paquetes que no son necesarios en el sistema:

```
sudo apt-get autoremove -y
```

Ahora instala el kernel i386:

```
sudo apt-get install -y linux-image-686
```

A continuación reinicia el equipo:

```
sudo reboot
```

Comprueba que está el nuevo kernel funcionando con:

```
uname -r
```

Aquí puede ocurrir que esté una versión "cloud" del kernel amd64, pero no hay problema, como ya hay una entrada en "/boot/initrd.img-4.19.0-11-686" al haber realizado la instalación del otro kernel (i386), en el siguiente paso que se eliminan todos los paquetes amd64 incluido estos kernel, se sustituirá automáticamente por el de i386.

Una vez este el kernel i386 instalado borra todos los paquetes amd64:

```
sudo apt-get remove -y `dpkg -l | grep '^.i' | awk '{print $2}' | grep :amd64`
```

Reinicia el equipo para asegurar el cambio de kernel si fuera necesario.

```
sudo reboot
```

### Borrado de la arquitectura amd64

Una vez realizado todo lo anterior se puede remover la arquitectura amd64 con:

```
sudo dpkg --remove-architecture amd64
```

Con esto el equipo quedará trasnformado por completo a una arquitectura i386.

***

Muchas gracias por leer hasta aquí espero que haya servido de ayuda. Un saludo.