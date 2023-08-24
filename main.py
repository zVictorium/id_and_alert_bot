import discord
from discord import app_commands as cmds
from discord.ext import commands as discord_commands


from commands import *
from settings import *


bot = discord_commands.Bot(
    command_prefix='/',
    intents=discord.Intents.all()
)


@bot.event
async def on_ready():

    print(LOGIN_MESSAGE.format(bot=bot.user))

    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            name=BOT_ACTIVITY,
            type=discord.ActivityType.listening,
        )
    )

    try:
        synced = await bot.tree.sync()
        print(SYNC_COMMANDS_MESSAGE.format(n=len(synced)))
    except Exception as exception:
        print(exception)


@bot.tree.command(name=PING_COMMAND, description=PING_DESCRIPTION)
async def ping(interaction: discord.Interaction):
    message = PING_MESSAGE.format(mention=interaction.user.mention)
    await interaction.response.send_message(message, ephemeral=True)


@bot.tree.command(name=SHOW_ID_COMMAND, description=SHOW_ID_DESCRIPTION)
async def dni(interaction: discord.Interaction):
    await show_id(interaction)


@bot.tree.command(name=CREATE_ID_COMMAND, description=CREATE_ID_DESCRIPTION)
@cmds.describe(
    nombre=NAME_DESCRIPTION,
    apellido=SURNAME_DESCRIPTION,
    nacimiento=BIRTH_DESCRIPTION,
    genero=GENDER_DESCRIPTION
)
async def dni_crear(
    interaction: discord.Interaction,
    nombre: str,
    apellido: str,
    nacimiento: str,
    genero: str
):
    await create_id(interaction, nombre, apellido, nacimiento, genero)


@bot.tree.command(name=EDIT_ID_COMMAND, description=EDIT_ID_DESCRIPTION)
@cmds.describe(
    usuario=USER_DESCRIPTION,
    nombre=NAME_DESCRIPTION,
    apellido=SURNAME_DESCRIPTION,
    nacimiento=BIRTH_DESCRIPTION,
    genero=GENDER_DESCRIPTION
)
async def dni_editar(
    interaction: discord.Interaction,
    usuario: discord.User,
    nombre: str = '',
    apellido: str = '',
    nacimiento: str = '',
    genero: str = ''
):
    await edit_id(interaction, usuario, nombre, apellido, nacimiento, genero)


@bot.tree.command(name=CLEAR_ID_COMMAND, description=CLEAR_ID_DESCRIPTION)
@cmds.describe(
    usuario=USER_DESCRIPTION
)
async def dni_clear(
    interaction: discord.Interaction,
    usuario: discord.User
):
    await clear_id(interaction, usuario)


@bot.tree.command(name=POLL_COMMAND, description=POLL_DESCRIPTION)
async def poll_cmd(interaction: discord.Interaction):
    await poll(interaction)


@bot.tree.command(name=SERVER_OPEN_COMMAND, description=SERVER_OPEN_DESCRIPTION)
async def server_open_cmd(interaction: discord.Interaction):
    await server_open(interaction)


@bot.tree.command(name=RESET_COMMAND, description=RESET_DESCRIPTION)
async def reset_cmd(interaction: discord.Interaction):
    await reset(interaction)


@bot.tree.command(name=SERVER_CLOSE_COMMAND, description=SERVER_CLOSE_DESCRIPTION)
async def server_close_cmd(interaction: discord.Interaction):
    await server_close(interaction)


@bot.tree.command(name=MAINTENANCE_COMMAND, description=MAINTENANCE_DESCRIPTION)
async def maintenance_cmd(interaction: discord.Interaction):
    await maintenance(interaction)


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
