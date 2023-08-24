
# DISCORD BOT

DISCORD_TOKEN = 'NTg3NzA1Nzg0Nzg4MzIwMzUy.GfZzAG.YiN0NqpOstRsZy6PF3hhAJKr0ThJzwg_pdz53c'

BOT_ACTIVITY = 'DNIs y alertas'

LOGIN_MESSAGE = '¡Iniciado sesión como {bot}!'
SYNC_COMMANDS_MESSAGE = 'Se han sincronizado {n} comandos.'
COMMAND_LOG = 'El comando /{command} ha sido activado por {user}.'


# COMANDOS

# Sobre DNIs

CREATE_ID_COMMAND = 'crear-dni'
CREATE_ID_DESCRIPTION = 'Crea tu DNI'

SHOW_ID_COMMAND = 'ver-dni'
SHOW_ID_DESCRIPTION = 'Ves tu DNI'

EDIT_ID_COMMAND = 'editar-dni'
EDIT_ID_DESCRIPTION = 'Edita un DNI'

REMOVE_ID_COMMAND = 'eliminar-dni'
REMOVE_ID_DESCRIPTION = 'Elimina un DNI'

HELP_ID_COMMAND = 'help-dni'
HELP_ID_DESCRIPTION = 'Muestra todos los comandos acerca del DNI'

USER_DESCRIPTION = 'Usuario del DNI'
NAME_DESCRIPTION = 'Nombre'
SURNAME_DESCRIPTION = 'Apellido'
BIRTH_DESCRIPTION = 'Fecha de nacimiento'
GENDER_DESCRIPTION = 'Género'

# Sobre Embeds

POLL_COMMAND = 'encuesta'
POLL_DESCRIPTION = 'Realiza una encuesta'

SERVER_OPEN_COMMAND = 'servidor-abierto'
SERVER_OPEN_DESCRIPTION = 'Alerta de servidor abierto'

SERVER_CLOSE_COMMAND = 'servidor-cerrado'
SERVER_CLOSE_DESCRIPTION = 'Alerta de servidor cerrado'

RESET_COMMAND = 'reinicio'
RESET_DESCRIPTION = 'Alerta de reinicio'

MAINTENANCE_COMMAND = 'mantenimiento'
MAINTENANCE_DESCRIPTION = 'Alerta de mantenimiento'

GREEN_ALERT_COMMAND = 'alerta-verde'
GREEN_ALERT_DESCRIPTION = 'Muestra la alerta verde.'

YELLOW_ALERT_COMMAND = 'alerta-amarilla'
YELLOW_ALERT_DESCRIPTION = 'Muestra la alerta amarilla.'

ORANGE_ALERT_COMMAND = 'alerta-naranja'
ORANGE_ALERT_DESCRIPTION = 'Muestra la alerta naranja.'

RED_ALERT_COMMAND = 'alerta-roja'
RED_ALERT_DESCRIPTION = 'Muestra la alerta roja.'

NEUTRAL_ALERT_COMMAND = 'alerta-neutra'
NEUTRAL_ALERT_DESCRIPTION = 'Muestra la alerta neutra.'


# MENSAJES:

# Ver DNI

MISSING_ID = 'No has creado un DNI aún.'

ID_MESSAGE_TITLE = '__**DNI de {name} {surname}**__'
ID_MESSAGE_AUTHOR = 'DNI de {username}'
ID_MESSAGE_FULLNAME = 'Nombre completo'
ID_MESSAGE_GENDER = 'Género'
ID_MESSAGE_BIRTH = 'Fecha de nacimiento'
ID_MESSAGE_ID = 'DNI'

# Crear DNI

WRONG_NAME = 'El nombre o el apellido no puede contener espacios.'
WRONG_BIRTH = 'No has introducido una fecha de nacimiento válida. (dd/mm/yyyy)'
WRONG_GENDER = 'No has introducido un género válido. ("Hombre", "Mujer" u "Otro")'

# Editar DNI

EDIT_FAIL = 'Tienes que editar al menos un valor.'
MISSING_USER_ID = 'El usuario no tiene ningún DNI creado.'

# Eliminar DNI

ID_REMOVED = 'DNI eliminado correctamente.'

# Ayuda DNI

ID_HELP = f'''
__**Comandos de DNI**__
</{HELP_ID_COMMAND}:1144342159026307147> _{HELP_ID_DESCRIPTION}_
</{SHOW_ID_COMMAND}:1144342159026307144> _{SHOW_ID_DESCRIPTION}_
</{CREATE_ID_COMMAND}:1144342159026307143> _{CREATE_ID_DESCRIPTION}_
</{EDIT_ID_COMMAND}:1144342159026307145> _{EDIT_ID_DESCRIPTION}_
</{REMOVE_ID_COMMAND}:1144342159026307146> _{REMOVE_ID_DESCRIPTION}_
'''


# EMBEDS

EMBED_LOG = '✅ Mensaje creado exitosamente.'
EMBED_FOOTER = 'Staff: {author}'

# Encuesta

POLL_PING = '@here'
POLL_TITLE = '🟠   __¿Quieres que se abra el servidor?__   🟠'
POLL_CONTENT = '¡Pues vota!\nMínimo 5 reacciones'
POLL_COLOR = 'f4900c'
POLL_REACTION = '👍'

# Avisos de servidor

SERVER_OPEN_PING = '@everyone'
SERVER_OPEN_TITLE = '🟩   __Servidor abierto__   🟩'
SERVER_OPEN_CONTENT = 'Únete con el código GLZRP en ER:LC\nSi necesitas ayuda pon !mod en el chat y te ayudaremos!'
SERVER_OPEN_COLOR = '78b159'

SERVER_CLOSE_PING = '@here'
SERVER_CLOSE_TITLE = '🟥   __Servidor cerrado__   🟥'
SERVER_CLOSE_CONTENT = 'Gracias por rolear con nosotros, sal sin cortar rol.\n¡Recuerda que tenemos canales para conocer gente OOC!'
SERVER_CLOSE_COLOR = 'e1264f'

RESET_PING = '@here'
RESET_TITLE = '🔧   __Reinicio del servidor__'
RESET_CONTENT = 'Para mejorar la experiencia IG se va a reiniciar el servidor, tienen 2 minutos para el kick.'
RESET_COLOR = '8899a6'

MAINTENANCE_PING = '@everyone'
MAINTENANCE_TITLE = '🔨   __Mantenimiento__'
MAINTENANCE_CONTENT = 'Se están realizando trabajos de mantenimiento para garantizar la calidad del servicio. El servidor permanecerá cerrado hasta nuevo aviso.'
MAINTENANCE_COLOR = 'f4900c'

# Alertas

GREEN_ALERT_PING = ''
GREEN_ALERT_TITLE = '🟢   __Alerta Verde__'
GREEN_ALERT_CONTENT = 'Galicia está tranquila, los cuerpos de seguridad solo podrán llevar Glock 17.'
GREEN_ALERT_COLOR = '78b159'

YELLOW_ALERT_PING = ''
YELLOW_ALERT_TITLE = '🟡   __Alerta Amarilla__'
YELLOW_ALERT_CONTENT = 'Galicia está un poco descontrolada, se podrá llevar el fusil MP5 en la mano (también Glock 17 opcional).'
YELLOW_ALERT_COLOR = 'fdcb58'

ORANGE_ALERT_PING = ''
ORANGE_ALERT_TITLE = '🟠   __Alerta Naranja__'
ORANGE_ALERT_CONTENT = 'Galicia está bastante descontrolada, los cuerpos de seguridad y los conductores tendrán que llevar MP5 y el copiloto M-4A1. Se podrá registrar a cualquier sujeto sospechoso.'
ORANGE_ALERT_COLOR = 'f4900c'

RED_ALERT_PING = ''
RED_ALERT_TITLE = '🔴   __Alerta Roja__'
RED_ALERT_CONTENT = 'Galicia está en graves problemas, tendrás que ir al hospital y esperar a que se baje la alerta. Los cuerpos de seguridad tendréis que usar G-36 o M-4A1, podréis registrar y parar a cualquier persona.'
RED_ALERT_COLOR = 'dd2e44'

NEUTRAL_ALERT_PING = ''
NEUTRAL_ALERT_TITLE = '⬜   __Alerta Blanca__'
NEUTRAL_ALERT_CONTENT = 'La ciudad está tranquila. Se puede vivir con normalidad. Habrá siempre 2 agentes en comisaría para gestiones como cambios en el DNI, denuncias, etc. Los cuerpos de seguridad llevarán sus armas reglamentarias. No se desplegarán unidades especiales a menos que ponga en peligro la integridad total de los ciudadanos.'
NEUTRAL_ALERT_COLOR = 'e6e7e8'


# CONSTANTES

DISCORD_LOGS = False
ID_DATA_FILENAME = 'data'

NAME = 'name'
SURNAME = 'surname'
BIRTH = 'birth'
GENDER = 'gender'
ID = 'id'

VALID_GENDERS = [
    'Hombre',
    'Mujer',
    'Otro'
]
