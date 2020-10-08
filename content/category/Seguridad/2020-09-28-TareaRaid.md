---
title: Tareas con RAID5
author: Adrián Rodríguez Povea
Summary:Buenas! En esta ocasión vamos a realizar un RAID5 y vamos a realizar varias pruebas. Utilizaremos RAID software en Linux con `mdadm`.

---

Buenas! En esta ocasión vamos a realizar un RAID5 y vamos a realizar varias pruebas. Utilizaremos RAID software en Linux con `mdadm`.

***

## Preparación para la tarea sobre RAID5

Para realizar esta tarea se va a utilizar una máquina virtual con vagrant-libvirt la configuración de vagrantfile es la siguiente:

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider :libvirt do |libvirt|
    libvirt.storage :file, :size => '1G'
    libvirt.storage :file, :size => '1G'
    libvirt.storage :file, :size => '1G'
    libvirt.storage :file, :size => '1G'
    libvirt.storage :file, :size => '1G'
  end
  config.vm.box = "debian/buster64"
end
```

Como podemos observar en el fichero agregamos 5 discos para realizar distintas pruebas a lo largo del ejercicio.

Una vez iniciada la máquina deberías obtener con el comando `lsblk` lo siguiente:

![lsblk]({{ site.baseurl }}/assets/img/TareaRAID5/lsblk.png)  

Lo siguiente es instalar el paquete `mdadm`, si no lo tenéis ya instalado en la máquina virtual:

```bash
sudo apt update && sudo apt install -y mdadm
```

***

## Tareas RAID5

#### Tarea 1: Crea una raid llamado "md5" con los discos que hemos conectado a la máquina. ¿Cuántos discos tienes que conectar? ¿Qué diferencia existe entre el RAID 5 y el RAID1?.    

Para el RAID5 hay que conectar 3 discos, es decir tiene en total una capacidad de 2GB, para hacer esto utiliza el siguiente comando:

```bash
sudo mdadm -C /dev/md5 --level=RAID5 --raid-devices=3 /dev/vdb /dev/vdc /dev/vdd
```
Si realizas de nuevo un `lsblk` obtendrás algo como esto:

![lsblk2]({{ site.baseurl }}/assets/img/TareaRAID5/lsblk2.png)

La diferencia entre RAID5 y RAID1 es:

En RAID5 los bloques estan distribuidos entre los 3 discos(los mínimos en RAID5) y soporta la pérdida total de unos de ellos, ya que distribuye la paridad entre los 3 dispositivos, pudiendo con dos recuperar toda la información.

En RAID1 se utilizan dos discos y uno es una copia exacta del otro, tiene ventajas en velocidades de lectura, ya que se puede leer de los dos discos, pero tiene desventaja en la escritura ya debe escribir en ambos discos la misma información.

#### Tarea 2: Comprueba las características del RAID. Comprueba el estado del RAID. ¿Qué capacidad tiene el RAID que hemos creado?.  

La capacidad es de 2GB, para comprobar el estado del RAID5 se consulta un fichero y para los detalles un comando: 

- Consultando el fichero `/etc/proc/mdstat` para ver su estado:

```bash
sudo cat /proc/mdstat
```

- Consultando los detalles:

```bash
sudo mdadm -D /dev/md5
```

En la siguiente imagen se pueden ver tanto el estado como los detalles:

![mdadmstatus]({{ site.baseurl }}/assets/img/TareaRAID5/comprobacionstadoraid.png)

#### Tarea 3: Crea un volumen lógico (LVM) de 500MB en el RAID5.    

Para esto hay que añadir el RAID5 a los volúmenes físicos, crear un grupo de volúmenes que utilize ese dispositivo y luego crear el volumen lógico:

```bash
sudo pvcreate /dev/md5
sudo vgcreate tareas /dev/md5
sudo lvcreate tareas -L 500M -n tarea3
```

Quedando como en la siguiente imagen:

![Vlogico]({{ site.baseurl }}/assets/img/TareaRAID5/Vlogico.png)

#### Tarea 4: Formatea ese volumen con un sistema de archivo `xfs`.    

Realiza el siguiente comando:

```bash
sudo mkfs.xfs /dev/tareas/tarea3
```

#### Tarea 5: Monta el volumen en el directorio `/mnt/RAID5` y crea un fichero. ¿Qué tendríamos que hacer para que este punto de montaje sea permanente?.

Para ello:

```bash
mkdir /mnt/RAID5
sudo mount -t xfs /dev/tareas/tarea3 /mnt/RAID5
touch /mnt/RAID5/fich.txt
```

Para que fuera permanente tendrías que incluir este montaje en el fichero `fstab`.    

#### Tarea 6: Marca un disco como estropeado. Muestra el estado del raid para comprobar que un disco falla. ¿Podemos acceder al fichero?.    

Para marcar un disco, por ejemplo `vdb` como fallido utiliza:

```bash
sudo mdadm --manage /dev/md5 --fail /dev/vdb
```

Luego mira el estado con:

```bash
cat /proc/mdstat
```

Mostrará algo similar a la siguiente imagen donde se observa que el disco esta marcado como fallido:

![fallovdb]({{ site.baseurl }}/assets/img/TareaRAID5/fallovdb.png)

El fichero se puede seguir visualizando sin problema.

#### Tarea 7: Una vez marcado como estropeado, lo tenemos que retirar del raid.   

Para ello utiliza el siguiente comando:

```bash
sudo mdadm --manage /dev/md5 --remove /dev/vdb
``` 

Observamos de nuevo el estado del RAID5 y mostrará lo siguiente:

```bash
cat /etc/proc/mdstat
```

![removevdb]({{ site.baseurl }}/assets/img/TareaRAID5/removevdb.png)


#### Tarea 8: Imaginemos que lo cambiamos por un nuevo disco nuevo (el dispositivo de bloque se llama igual), añádelo al array y 
comprueba como se sincroniza con el anterior. 

Para ello en este caso con un nuevo disco "vde":

```bash
sudo mdadm --manage /dev/md5 --add /dev/vde
```

Automáticamente se sincroniza con el raid, observa los cambios con:

```bash
lsblk
cat /proc/mdstat
```

Obteniendo algo similar a lo siguiente:

![agregandovde]({{ site.baseurl }}/assets/img/TareaRAID5/agregandovde.png)

#### Tarea 9: Añade otro disco como reserva. Vuelve a simular el fallo de un disco y comprueba como automáticamente se realiza la sincronización con el disco de reserva.

Realiza los siguiente comandos para añadir el disco como reserva:

```bash
mdadm --manage /dev/md5 -add /dev/vdf
```

Puedes comprobar que se ha añadido como "SPARE" comprobando el estado o los detalles del RAID5 con los siguientes comandos:

```bash
sudo mdadm -D /dev/md5
```
O
```bash
cat /proc/mdstat
```

Ahora vuelve a marcar otro dispositivo como fallido esta vez `vdc`:

```bash
sudo mdadm --manage /dev/md5 --fail /dev/vdc
```

Como podemos ver en la siguiente imagen el disco pasa de SPARE (S) a activo y el otro se marca como FAIL (F)

![SPAREautilizado]({{ site.baseurl }}/assets/img/TareaRAID5/SPAREautilizado.png)

Como repunte, si quisieras que el disco se agrege como dispositivo adicional para aumentar las dimesiones del raid, después de agregarlo, realiza el siguiente comando:

```bash
sudo mdadm --grow /dev/md5 --raid-devices=4
```

Y luego aumentar el raid a la máxima capacidad disponible con:

```bash
sudo mdadm --grow /dev/md5 -z max
```

#### Tarea 10: Redimensiona el volumen y el sistema de archivo de 500MB al tamaño del raid. 

Con los siguientes comandos podras redimensionar el volumen y luego redimensionar el sistema de ficheros:

```bash
sudo lvextend -L +1.5G /dev/tareas/tarea3 
sudo xfs_growfs /mnt/RAID5/
```

Recalcar que con `xfs`se puede realizar esta acción en caliente con otros sistemas de ficheros podría ocasionar errores o pérdida de datos.

Al finalizar todas las tareas en este orden la orden `lsblk -f` debería mostrar algo así:

![lsblkfinal]({{ site.baseurl }}/assets/img/TareaRAID5/lsblkfinal.png)

***
    
Muchas gracias por leer hasta aquí espero que haya servido de ayuda. Un saludo.    
