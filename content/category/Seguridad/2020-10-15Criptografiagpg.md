---
title: Criptografía: GPG y OPENSSL
author: Adrián Rodríguez Povea
status: published
Summary: Buenas! En esta ocasión se van a realizar una serie de pruebas con GPG y OPENSSL.

---

Buenas! En esta ocasión se van a realizar una serie de pruebas con GPG y OPENSSL.

***

## GPG

#### Creación de claves pública y privada:

Para ello se realiza el siguiente comando, el cual te realizará una serie de preguntas:
```
gpg --gen-key
```

Si quieres crearla con mas detalles y diálogo realiza:
```
gpg --full-generate-key
```

Al final mostrará algo como esto:

![clavepubl]({static}/images/Criptografía/clavepublicaadri.png) 

Todo lo referente a las claves "GPG" esta en el directorio "~/.gnupg" de cada usuario.

Para listar las claves públicas utiliza el comando:
```
gpg --list-keys
``` 
Los datos mostrados son:

* El tipo de clave y el sistema de criptografía que tiene. Por ejemplo "rsa4096".
* El uid, número que identifica la clave, para identificarla se pueden utilizar los últimos 8 dígitos.
* El nombre del propietario junto con su correo y comentario si dispone de él.
* Confianza que se tiene sobre esa clave.
* Fecha de validez si dispone de ella.

Para darle fecha de validez a la clave, cuando se genera la clave con "gpg --gen-key" o "gpg --full-generate-key" preguntará algo como esto:

```console
Por favor, especifique el período de validez de la clave.
         0 = la clave nunca caduca
      <n>  = la clave caduca en n días
      <n>w = la clave caduca en n semanas
      <n>m = la clave caduca en n meses
      <n>y = la clave caduca en n años
¿Validez de la clave (0)? 1M
```
En el ejemplo de arriba al final se le asignó 1 mes.

Para ver las claves privadas:
```
gpg --list-secret-keys
```

#### Importar y Exportar claves públicas.

A continuación se mostrarán los comandos para exportar una clave pública en formato ASCII. Para ello:

```
gpg --export -a "uid_o_nombre usuario" > clavepublica.asc
```

Como se muestra en la siguiente imagen:

![exportclavepub]({static}/images/Criptografía/expportarclavepub.png) 

A continuación se mostrarán los comando para importar la clave de un compañero a nuestro anillo de claves:

```
gpg --import pepito_perez.asc
```

Como se muestra en la siguiente imagen:

![importpepito]({static}/images/Criptografía/importpepito.png) 

#### Cifrado y Descifrado de documentos

A continuación se muestran los comandos para cifrar y descifrar documentos:

Para cifrar un documento:
```
gpg -e mensaje.txt
```
Esto pedirá el uid del destinatario en nuestro caso el de Pepito Pérez, en la siguiente imagen se muestra todo el proceso y el fichero "mensaje.txt.gpg":

![gpgcifrado]({static}/images/Criptografía/gpgcifrado.png) 

También se puede utilizar el comando con argumentos para que no sea de forma interactiva:

```
gpg -e -u "Adrian Rodriguez" -r "pepito perez"
```

Cualquiera que no esté en la lista al crear el mensaje cifrado, no puede descifrarlo. Le lanzará un mensaje de error del estilo:
```
gpg: descifrado fallido: No secret key
```
Una vez Pepito tiene el mensaje cifrado utiliza:

```
gpg -o mensaje.txt -d mensaje.txt.gpg 
```

Al realizar este comando si tiene contraseña, la pedirá y luego descifrará el mensaje. Como se muestra en la siguiente imagen:

![gpgdescrifrado]({static}/images/Criptografía/decryptmens.png)

#### Borrar claves públicas o privadas:

Para borrar las claves públicas utiliza el comando:

```
gpg --delete-key "uid_o_nombreusuario"
```

Para borrar las claves privadas utiliza:

```
gpg --delete-secret-key "uid_onombreusuario"
```

#### Exportar clave a un servidor público de claves PGP

Lo primero que se va a realizar es la clave de revocación por si existe algun problema con la clave, para ello:

```
gpg -gen-revoke "uid_o_nombreusuarito" > cert_revoc.asc
```
También se puede utilizar:
```
gpg --output cer_revoc.asc --gen-revoke "uid_o_nombreusuario"
```
Al realizar estos comandos preguntará la razón de la revocación como se muestra a continuación:
```
¿Crear un certificado de revocación para esta clave? (s/N) s
Por favor elija una razón para la revocación:
  0 = No se dio ninguna razón
  1 = La clave ha sido comprometida
  2 = La clave ha sido reemplazada
  3 = La clave ya no está en uso
  Q = Cancelar
(Probablemente quería seleccionar 1 aquí)
¿Su decisión? 1
Introduzca una descripción opcional; acábela con una línea vacía:
> 
Razón para la revocación: La clave ha sido comprometida
(No se dió descripción)
¿Es correcto? (s/N) s
se fuerza salida con armadura ASCII.
```

Para utilizar esto solo hay que importar el certificado generado y se anulará la clave, si está en un servidor público hay que volver a subirla una vez revocada.

Una vez se ha generado el certificado de revocación estos son los comandos necesarios para subir tu clave pública a un servidor, en este caso "pgp.rediris.es":

```
gpg --keyserver gpg.rediris.es --send-keys D4BB0593 
```

Para importar una clave de un servidor:

```
gpg --recv-keys --keyserver pgp.rediris.es D4BB0593
```

En las siguientes imágenes se muestra como un usuario, sube la clave y otro importa esta clave desde el servidor:

![subirclaveserv]({static}/images/Criptografía/subirclave.png)
![importarclaveserv]({static}/images/Criptografía/importarclave.png)

## Cifrado OPENSSL

A continuación se muestran los comandos para crear una clave privada en openssl y generar una clave pública de la clave privada.

Crear clave privada:
```
openssl genrsa -out key.pem 2048
```

Crear clave pública:

```
openssl rsa -in key.pem -pubout -out key.public.pem
```

Se puede también encriptar la clave privada con una contraseña con el siguiente comando:

```
openssl rsa -in key.pem -des3 -out enc-key.pem
```

Para cifrar un documento(Con la clave pública del destinatario):

```
openssl rsautl -encrypt -inkey pub-key.pem -pubin -in mensaje.txt -out mensaje.txt.enc
```

Para descifrar un mensaje sería lo mismo pero en el destinatario utilizando su clave privada:

```
openssl rsautl -decrypt -inkey key.pem -in mensaje..txt.enc -out mensaje.txt
```

A continuación se muestra un ejemplo en las siguientes imagenes:


![openssl1]({static}/images/Criptografía/openssl1.png)
![openssl2]({static}/images/Criptografía/openssl2.png)

Como dato extra también es posible cifrar con la clave privada y que descifren con la clave pública aunque es menos utilizado:

Cifrado con clave privada:

```
openssl rsautl -inkey key.pem -in mensaje.txt -sign > mensaje.txt.enc
```

Descifrado con clave pública:

```
openssl rsautl -inkey pub-key.pem -pubin -in mensaje.txt.enc -out mensaje.txt
```