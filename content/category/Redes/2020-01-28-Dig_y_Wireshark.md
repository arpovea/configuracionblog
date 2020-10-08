---
title: Probando Dig y Wireshark
author: Adrián Rodríguez Povea
Summary: Buenas! En esta ocasión vamos a probar un poco el comando dig y el programa Wireshark, con los cuales realizaremos consultas DNS e investigaremos un poco el tráfico de una petición a una página web.

---

Buenas! En esta ocasión vamos a probar un poco el comando dig y el programa Wireshark, con los cuales realizaremos consultas DNS e investigaremos un poco el tráfico de una petición a una página web.

***

## DIG    
Se va a realizar una petición DNS con el comando dig a las páginas www.marca.com y www.elmundo.es:

```bash
dig www.marca.com
```
Captura de pantalla correspondiente:    

![dig1]({{ site.baseurl }}/assets/img/DigyWireshark/digmarca.png) 

```bash
dig www.elmundo.com
```
Captura de pantalla correspondiente:    

![dig2]({{ site.baseurl }}/assets/img/DigyWireshark/digelmundo.png)     

Como se puede observar en las imágenes ambas webs estan alojadas en el servidor `151.101.133.50` con el CNAME(alias del dominio) "unidadeditorial.map.fastly.net".    

***

## Wireshark

A continuación se realiza una captura del tráfico con Wireshark accediendo al sitio www.marca.com.
En ella podemos observar lo siguiente:

La petición y respuesta DNS:

![dns1]({{ site.baseurl }}/assets/img/DigyWireshark/capturadnsmarca1.png)
![dns2]({{ site.baseurl }}/assets/img/DigyWireshark/capturadns2.png)
![dns3]({{ site.baseurl }}/assets/img/DigyWireshark/capturadns3.png)

La primera conexión TSL, puesto que es una página que tiene seguridad HTTPS, con esto el cliente le pide los certificados a la página para poder conectarse de forma segura:    

Mensajes del cliente:    

![TSL1]({{ site.baseurl }}/assets/img/DigyWireshark/clienthellow1.png)

![TSL2]({{ site.baseurl }}/assets/img/DigyWireshark/clienthellow2.png)

Mensajes del servidor:    

![TSL3]({{ site.baseurl }}/assets/img/DigyWireshark/serverhellow.png)

![TSL4]({{ site.baseurl }}/assets/img/DigyWireshark/serverhellow2.png)

Ya que es una página con seguridad HTTPS no podemos sacar mucha información, de todas formas dejo por aquí los filtros de Wireshark para páginas HTTP:   

	-http —> Protocolo HTTP

	-http.host==”www.google.com” —> Queremos ver los paquetes que tengan a Google como host.

	-http.date==”Wed, 30 Mar 2011 22:40:55 GMT” —> Paquetes con respecto a una fecha

	-http.content_type==”application/json” —> Según el tipo. Hay más tipos.

	-http.content_type==”image/png” —> Imágenes PNG

	-http.content_type==”image/gif” —> Imágenes GIF

	-http.content_type==”image/jpeg” —> Imágenes JPEG

	-http.content_type==”text/html” —> Archivos HTML

	-http.content_type==”text/css” —> Hojas de estilo CSS

	-http.content_type==”video/quicktime” —> Vídeos

	-http.content_type==”application/zip” —> Archivos ZIP

	-http.request.method==”GET” —> Tipo de Petición GET

	-http.request.method==”POST” —> Tipo de Petición POST

	-http.user_agent contains “Mozilla” —> Navegador Mozilla

	-http.request.uri!=*—> Con esto me libro de los paquetes “NOTIFY * HTTP…”

	-http.request.uri matches “[0-9]” —> Uso de expresiones regulares.

Estos son solo algunos ejemplos. ¡Existen muchos mas!    

***

Muchas gracias por leer hasta aquí, espero que sirva de ayuda. Nos vemos en el siguiente post.