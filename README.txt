Heroes Never Die, un proyecto realizado por:

- Jesús Borrego
- Álvaro Marcos

- Carlos Guzmán

- Luis Gutiérrez



Resumen de la ejecución:

El pollDM.py se conecta mediante el protocolo PUSH al puerto 5559 del localhost,
y va recibiendo los últimos 20 mensajes directos que ha recibido cada 5 segundos.

Envía los mensajes al zmq device de tipo STREAMER, que se encarga de redirigir
los mensajes a los diferentes workers asociados.


A cada worker le llegará una carga de trabajo en función de lo ocupados que
esten los demás workers, y cada uno realizará la misma función:


1) Comprueba que el DM es correcto y que los datos se pueden extraer

2) Extrae los datos y los almacena en listas auxiliares

3) Llama a una subrutina que crea la gráfica con el plot y la sube a imgur



Paralelo a todo eso, tenemos un proceso al que hemos llamado enviar.py que
abre el fichero que controla las gráficas que hemos subido a imgur

(el esquema del mensaje en cada línea es: 'link' 'id_usuario' 'heroe_evaluado').

A medida que evalúa las graficas subidas, va enviando DMs a los usuarios que
han solicitado la información en forma de gráfica y, 
una vez ha terminado de
procesar todas las imágenes, limpia el archivo para indicar que las imágenes
ya se han enviado.



Uso de Heroes Never Die:


CASE_LOCK SENSITIVE

Enviar un mensaje directo a la cuenta @AnalyticsOW con la siguiente
estructura:
'Battle Tag' 'Modo de juego' 'Heroe'



Requisitos para el funcionamiento del bot: 
Para obtener las estadisticas
de un heroe en un modo de juego especifico, 
has de haber jugado mínimo 1h
con dicho Heroe en Partida Rápida, o 10 minutos en Competitivo, 
de otro modo
el API considera que 'no has explotado lo suficiente al heroe' como para que
se muestren todas sus estadísticas en el JSON


Battle Tag: Nombre y número separados por un guión (ej: Usuario-1111)

Modo de juego: competitive / quickplay

Heroe: en minúsculas, sin caracteres especiales (ej: torbjorn)

SOLO CREADO PARA USUARIOS DE OVERWATCH EN PC Y EU