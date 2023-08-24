
# DISCORD BOT

DISCORD_TOKEN = 'NTg3NzA1Nzg0Nzg4MzIwMzUy.GfZzAG.YiN0NqpOstRsZy6PF3hhAJKr0ThJzwg_pdz53c'

BOT_ACTIVITY = 'DNIs y comandos'

LOGIN_MESSAGE = '¡Iniciado sesión como {bot}!'
SYNC_COMMANDS_MESSAGE = 'Se han sincronizado {n} comandos.'

# COMANDOS

PING_COMMAND = 'ping'
PING_DESCRIPTION = 'Pong!'
PING_MESSAGE = 'Pong! {mention}'

SHOW_ID_COMMAND = 'dni'
SHOW_ID_DESCRIPTION = 'Ver tu DNI'

CREATE_ID_COMMAND = 'dni-crear'
CREATE_ID_DESCRIPTION = 'Crear tu DNI'

EDIT_ID_COMMAND = 'dni-editar'
EDIT_ID_DESCRIPTION = 'Edita un DNI'

CLEAR_ID_COMMAND = 'dni-clear'
CLEAR_ID_DESCRIPTION = 'Elimina un DNI'

USER_DESCRIPTION = 'Usuario del DNI'
NAME_DESCRIPTION = 'Nombre'
SURNAME_DESCRIPTION = 'Apellido'
BIRTH_DESCRIPTION = 'Fecha de nacimiento'
GENDER_DESCRIPTION = 'Género'

POLL_COMMAND = 'encuesta'
POLL_DESCRIPTION = 'Mensaje de encuesta'

SERVER_OPEN_COMMAND = 'servidor-abierto'
SERVER_OPEN_DESCRIPTION = 'Mensaje de servidor abiero'

RESET_COMMAND = 'reinicio'
RESET_DESCRIPTION = 'Mensaje de reinicio'

SERVER_CLOSE_COMMAND = 'servidor-cerrado'
SERVER_CLOSE_DESCRIPTION = 'Mensaje de servidor cerrado'

MAINTENANCE_COMMAND = 'mantenimiento'
MAINTENANCE_DESCRIPTION = 'Mensaje de mantenimiento'

# MENSAJES:

# Ver DNI

MISSING_ID = 'No has creado un DNI aún.'

DNI_MESSAGE = '''
__**DNI de {user}**__
 ● **Nombre:** `{name}`
 ● **Apellido:** `{surname}`
 ● **Nacimiento:** `{birth}`
 ● **Género:** `{gender}`
 ● **DNI:** `{id}`
'''

# Crear DNI

WRONG_NAME = 'El nombre o el apellido no puede contener espacios.'
WRONG_BIRTH = 'No has introducido una fecha de nacimiento válida. (dd-mm-yyyy)'
WRONG_GENDER = 'No has introducido un género válido. ("Hombre", "Mujer" u "Otro")'

# Editar DNI

EDIT_FAIL = 'Tienes que editar al menos un valor.'
MISSING_USER_ID = 'El usuario no tiene ningún DNI creado.'

# Eliminar DNI

DNI_REMOVED = 'DNI eliminado correctamente.'


# EMBEDS

POLL_TITLE = 'Encuesta'
POLL_DESCRIPTION = 'Vota para esto.'
POLL_COLOR = 'dcdcaa'

SERVER_OPEN_TITLE = 'Servidor abierto'
SERVER_OPEN_DESCRIPTION = 'El servidor se ha iniciado.'
SERVER_OPEN_COLOR = '73c984'

RESET_TITLE = 'Reinicio'
RESET_DESCRIPTION = 'El servidor se va a reiniciar.'
RESET_COLOR = 'ffb517'

SERVER_CLOSE_TITLE = 'Servidor cerrado'
SERVER_CLOSE_DESCRIPTION = 'El servidor se ha cerrado.'
SERVER_CLOSE_COLOR = 'e1264f'

MAINTENANCE_TITLE = 'Mantenimiento'
MAINTENANCE_DESCRIPTION = 'El servidor está en mantenimiento.'
MAINTENANCE_COLOR = 'c965c9'

# CONSTANTES

DNI_DATA_FILENAME = 'data'

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
