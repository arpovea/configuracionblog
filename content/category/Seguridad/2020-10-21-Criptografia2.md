---
title: Tareas con RAID5
author: Adrián Rodríguez Povea
status: draft
Summary:Buenas! En esta ocasión vamos se van a realizar una serie de tareas con firmas electronicas, correo seguro, integridad de ficheros, "apt secure" y autentificación SSH.

---

Buenas! En esta ocasión vamos se van a realizar una serie de tareas con firmas electronicas, correo seguro, integridad de ficheros, "apt secure" y autentificación SSH.

***

Descarga una firma de un compañerp desde un servidor de claves gpg y importala a tu anillo de claves.

gpg --recv-keys --keyserver keys.gnupg.net 12B9A4F8

Firma esta clave de la siguiente forma:

gpg --edit-key 12B9A4F8

fpr -> para mirar la huella

sign -> para firmar

quit

gpg --list-key sign 12B9A4F8 -->lista la clave y sus firmas

***
    
Muchas gracias por leer hasta aquí espero que haya servido de ayuda. Un saludo.    
