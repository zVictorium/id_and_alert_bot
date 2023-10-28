# Bot de Discord con sistema de DNI y alertas

Este es un bot de Discord desarrollado en Python utilizando la librería discord.py.

## Descripción 

Este bot tiene varias funcionalidades:

- Comandos para crear, mostrar, editar y eliminar DNIs personalizados
- Comandos para enviar embeds con encuestas, alertas de colores, avisos de mantenimiento, etc.
- Almacenamiento de DNI en archivo JSON

## Instalación

1. Descarga este proyecto
2. Crea un bot en el [Portal de Desarrolladores de Discord](https://discordapp.com/developers)
3. Agrega el token del bot en el archivo `settings.py`
4. Instala las dependencias con `pip install -r requirements.txt` 
5. Ejecuta el bot con `python main.py`

## Uso

El prefijo del bot es `/`.

Todos los mensajes son editables a través del archivo `settings.py` sin necesidad de buscar dentro del código.
