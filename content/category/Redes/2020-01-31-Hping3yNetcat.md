---
title: Hping3 y NetCat
author: Adrián Rodríguez Povea
Summary: Buenas! En esta ocasión vamos a probar un poco el comando Hping3 y  NetCat, con los cuales realizaremos pruebas en un escenario creado en una máquina virtual con Mininet. Probaremos a modificar los paquetes de ping y a conectarnos a distintos puertos y realizar varias conexiones.

---

Buenas! En esta ocasión vamos a probar un poco el comando Hping3 y  NetCat, con los cuales realizaremos pruebas en un escenario creado en una máquina virtual con Mininet. Probaremos a modificar los paquetes de ping y a conectarnos a distintos puertos y realizar varias conexiones.

***

## Mininet

A continuación se expondra el escenario y los comandos que se van a utilizar en esta práctica:    

Esquema de escenario:    

`10.0.100.0/24 -> h1, h2 y r1`    
`10.0.110.0/24 -> r1 y r2`    
`10.0.120.0/24 -> r2 y r3`    
`10.0.130.0/24 -> h3, h4  y r3`    

![escenario]({static}/images/Hping3yNetCat/escenario.png)

Se dejan por aquí los enlaces a los scripts tanto del escenario como del despliegue en Mininet:    

[Scrip Escenario](https://github.com/arpovea/arpovea.github.io/blob/master/assets/img/Hping3yNetCat/escenariotrasnporte2.mn)

[Scrip Despliegue](https://github.com/arpovea/arpovea.github.io/blob/master/assets/img/Hping3yNetCat/escenariotrasnporte2.py)

Una vez desplegado el escenario los comandos para configurar la red en cada máquina son:    

```bash
#H1 
ip a add 10.0.100.3/24 dev h1-eth0
ip r add default via 10.0.100.1

#H2
ip a add 10.0.100.4/24 dev h2-eth0
ip r add default via 10.0.100.2

#R1
ip a add 10.0.110.1/24 dev r1-eth0
ip a add 10.0.100.1/24 dev r1-eth1
ip a add 10.0.100.2/24 dev r1-eth2
ip r add default via 10.0.110.2

#R2
ip a add 10.0.110.2/24 dev r2-eth0
ip a add 10.0.120.1/24 dev r2-eth1
ip r add 10.0.100.0/24 via 10.0.110.1
ip r add 10.0.130.0/24 via 10.0.120.2

#R3
ip a add 10.0.120.2/24 dev r3-eth0
ip a add 10.0.130.1/24 dev r3-eth1
ip a add 10.0.130.2/24 dev r3-eth2
ip r add default via 10.0.120.1

#H3
ip a add 10.0.130.3/24 dev h3-eth0
ip r add default via 10.0.130.1

#H4
ip a add 10.0.130.4/24 dev h4-eth0
ip r add default via 10.0.130.2
```    

***

## HPing3

Ahora se va a realizar con el comando HPing3 un Echo Request desde H1 hacia H4 capturando el tráfico en R3 con Wireshark:    

Comando H1:

```bash
hping3 -K 0 -c 5 10.0.130.4
```
La opción -K indica que utilice Echo Request, este vendria por defecto pero con esto se le especifica.    
La opción -c indica el número de paquetes que se enviarán en este caso "5".     

Estas son las capturas realizadas con Wireshark en R3:    

![echorequest1]({static}/images/Hping3yNetCat/capturaechorequest1.png)    
![echorequest2]({static}/images/Hping3yNetCat/capturaechorequest2.png)    

A continución cambiaremos la TTL para que no sea alcanzable H4:    

Comando H1:    

```bash
hping -K 0 --ttl 3 -c 3 10.0.130.4
```

La opcion --ttl cambia por defecto la ttl de "64"(por defecto) en "3" en este caso.

![TTL]({static}/images/Hping3yNetCat/TTL.png)

Como se puede observar en la imagen no llega a su destino.    


Ahora se intentará realizar una conexion desde el puerto "4000" al puerto "80" desde H1:    
```bash
hping3 -s 4000 -p 80 10.0.130.4
```

La opción -s indica el puerto base.    
La opción -p indica el puerto destino.    

Capturas en Wireshark:

![TCP4000-1]({static}/images/Hping3yNetCat/capturaTCP4000-1.png)    
![TCP4000-2]({static}/images/Hping3yNetCat/capturaTCP4000-2.png)    

Como se puede observar al no estar el puerto "80" activo se recibe la etiqueta [RST,ACK] que indica que no hay nada en ese puerto, si hubiera un servicio en ese puerto escuchando se mostraría la etiqueta [SYN,ACK].    


*** 

## NetCat

Con NetCat se creara un servidor TCP en el puerto "80" de H3 y se realizará una conexión desde H2, se capturará el tráfico con Wireshark en R3:    

Comando para el servidor TCP en H3:    
```bash
nc -l 80
```
Comando para realizar la conexión desde H2:    
```bash
nc 10.0.130.3 80
```
A continuación se escribe en H2 y aparecerá en H3 como muestra la siguiente imagen:

![TCPconexion]({static}/images/Hping3yNetCat/TCPconexion.png)    

Capturas de Wireshark:    

![netcap1]({static}/images/Hping3yNetCat/netcap1.png)    
![netcap2]({static}/images/Hping3yNetCat/netcat2.png)    
![mensaje1]({static}/images/Hping3yNetCat/mensaje1psh.png)    
![mensaje2]({static}/images/Hping3yNetCat/mensaje2psh.png)    

Como se puede obsevar en estas capturas se ve la conexión TCP con la etiqueta [SYN,ACK] y luego los mensajes enviados con la etiqueta [PSH,ACK].    

Ahora se cerrara la conexión y se mostrará la secuencia de cierre con Wireshark:    

![secuenciadecerrado]({static}/images/Hping3yNetCat/secuenciadecerrado.png)    

Aquí se observa la etiqueta [FIN,ACK] y sus respectivas respuestas, indicando el cierre de la conexión.    


Probaremos a realizar lo mismo pero con un servidor UDP en vez de TCP, esta vez el servidor en H1 y la conexión desde H4:    

Comando para el servidor UDP en H1:    
```bash
nc -u -l 80
```
Comando para realizar la conexión UDP desde H4:    
```bash
nc -u 10.0.130.3 80
```
A continuación se escribe en H4 y aparecerá en H1 como muestra la siguiente imagen:    

![UDPconexion]({static}/images/Hping3yNetCat/UDPconexion.png)    

Capturas de Wireshark:    

![UDP1]({static}/images/Hping3yNetCat/Netcatudp1.png)    
![UDP2]({static}/images/Hping3yNetCat/netcapUDP2.png)    

Con el protocolo UDP no se comprueban las mismas cosas que con el protocolo TCP, la única ventaja de UDP es que es más liviano y en algunas ocasiones tiene sus ventajas. Como se puede observar solo están los mensajes enviados desde H4 hacia H1.    

***

Muchas gracias por leer hasta aquí espero que sirva de ayuda. Un saludo.    
