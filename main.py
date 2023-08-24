import discord
from discord import app_commands as cmds
from discord.ext import commands as discord_commands

import commands
from settings import *


bot = discord_commands.Bot(
    command_prefix='!',
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


@bot.tree.command(name=CREATE_ID_COMMAND, description=CREATE_ID_DESCRIPTION)
@cmds.describe(
    nombre=NAME_DESCRIPTION,
    apellido=SURNAME_DESCRIPTION,
    nacimiento=BIRTH_DESCRIPTION,
    genero=GENDER_DESCRIPTION
)
async def create_id(
    interaction: discord.Interaction,
    nombre: str,
    apellido: str,
    nacimiento: str,
    genero: str
):
    print(COMMAND_LOG.format(command=CREATE_ID_COMMAND, user=interaction.user))
    await commands.create_id(interaction, nombre, apellido, nacimiento, genero)


@bot.tree.command(name=SHOW_ID_COMMAND, description=SHOW_ID_DESCRIPTION)
async def show_id(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=SHOW_ID_COMMAND, user=interaction.user))
    await commands.show_id(interaction)


@bot.tree.command(name=EDIT_ID_COMMAND, description=EDIT_ID_DESCRIPTION)
@cmds.describe(
    usuario=USER_DESCRIPTION,
    nombre=NAME_DESCRIPTION,
    apellido=SURNAME_DESCRIPTION,
    nacimiento=BIRTH_DESCRIPTION,
    genero=GENDER_DESCRIPTION
)
async def edit_id(
    interaction: discord.Interaction,
    usuario: discord.User,
    nombre: str = '',
    apellido: str = '',
    nacimiento: str = '',
    genero: str = ''
):
    print(COMMAND_LOG.format(command=EDIT_ID_COMMAND, user=interaction.user))
    await commands.edit_id(interaction, usuario, nombre, apellido, nacimiento, genero)


@bot.tree.command(name=REMOVE_ID_COMMAND, description=REMOVE_ID_DESCRIPTION)
@cmds.describe(
    usuario=USER_DESCRIPTION
)
async def remove_id(
    interaction: discord.Interaction,
    usuario: discord.User
):
    print(COMMAND_LOG.format(command=REMOVE_ID_COMMAND, user=interaction.user))
    await commands.remove_id(interaction, usuario)


@bot.tree.command(name=HELP_ID_COMMAND, description=HELP_ID_DESCRIPTION)
async def help_id(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=HELP_ID_COMMAND, user=interaction.user))
    await commands.help_id(interaction)


@bot.tree.command(name=POLL_COMMAND, description=POLL_DESCRIPTION)
async def poll(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=POLL_COMMAND, user=interaction.user))
    await commands.poll(interaction)


@bot.tree.command(name=SERVER_OPEN_COMMAND, description=SERVER_OPEN_DESCRIPTION)
async def server_open(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=SERVER_OPEN_COMMAND, user=interaction.user))
    await commands.server_open(interaction)


@bot.tree.command(name=SERVER_CLOSE_COMMAND, description=SERVER_CLOSE_DESCRIPTION)
async def server_close(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=SERVER_CLOSE_COMMAND, user=interaction.user))
    await commands.server_close(interaction)


@bot.tree.command(name=RESET_COMMAND, description=RESET_DESCRIPTION)
async def reset(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=RESET_COMMAND, user=interaction.user))
    await commands.reset(interaction)


@bot.tree.command(name=MAINTENANCE_COMMAND, description=MAINTENANCE_DESCRIPTION)
async def maintenance(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=MAINTENANCE_COMMAND, user=interaction.user))
    await commands.maintenance(interaction)


@bot.tree.command(name=GREEN_ALERT_COMMAND, description=GREEN_ALERT_DESCRIPTION)
async def green_alert(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=GREEN_ALERT_COMMAND, user=interaction.user))
    await commands.green_alert(interaction)


@bot.tree.command(name=YELLOW_ALERT_COMMAND, description=YELLOW_ALERT_DESCRIPTION)
async def yellow_alert(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=YELLOW_ALERT_COMMAND, user=interaction.user))
    await commands.yellow_alert(interaction)


@bot.tree.command(name=ORANGE_ALERT_COMMAND, description=ORANGE_ALERT_DESCRIPTION)
async def orange_alert(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=ORANGE_ALERT_COMMAND, user=interaction.user))
    await commands.orange_alert(interaction)


@bot.tree.command(name=RED_ALERT_COMMAND, description=RED_ALERT_DESCRIPTION)
async def red_alert(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=RED_ALERT_COMMAND, user=interaction.user))
    await commands.red_alert(interaction)


@bot.tree.command(name=NEUTRAL_ALERT_COMMAND, description=NEUTRAL_ALERT_DESCRIPTION)
async def neutral_alert(interaction: discord.Interaction):
    print(COMMAND_LOG.format(command=NEUTRAL_ALERT_COMMAND, user=interaction.user))
    await commands.neutral_alert(interaction)


if __name__ == '__main__':
    if DISCORD_LOGS:
        bot.run(DISCORD_TOKEN)
    else:
        bot.run(DISCORD_TOKEN, log_handler=None)
