import discord

from utils import Embed
from settings import *


async def poll(interaction: discord.Interaction):
    embed = Embed(
        title=POLL_TITLE,
        description=POLL_CONTENT,
        color=POLL_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    message = await interaction.channel.send(content=POLL_PING, embed=embed)
    await message.add_reaction(POLL_REACTION)


async def server_open(interaction: discord.Interaction):
    embed = Embed(
        title=SERVER_OPEN_TITLE,
        description=SERVER_OPEN_CONTENT,
        color=SERVER_OPEN_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=SERVER_OPEN_PING, embed=embed)


async def server_close(interaction: discord.Interaction):
    embed = Embed(
        title=SERVER_CLOSE_TITLE,
        description=SERVER_CLOSE_CONTENT,
        color=SERVER_CLOSE_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=SERVER_CLOSE_PING, embed=embed)


async def reset(interaction: discord.Interaction):
    embed = Embed(
        title=RESET_TITLE,
        description=RESET_CONTENT,
        color=RESET_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=RESET_PING, embed=embed)


async def maintenance(interaction: discord.Interaction):
    embed = Embed(
        title=MAINTENANCE_TITLE,
        description=MAINTENANCE_CONTENT,
        color=MAINTENANCE_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=MAINTENANCE_PING, embed=embed)


async def green_alert(interaction: discord.Interaction):
    embed = Embed(
        title=GREEN_ALERT_TITLE,
        description=GREEN_ALERT_CONTENT,
        color=GREEN_ALERT_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=GREEN_ALERT_PING, embed=embed)


async def yellow_alert(interaction: discord.Interaction):
    embed = Embed(
        title=YELLOW_ALERT_TITLE,
        description=YELLOW_ALERT_CONTENT,
        color=YELLOW_ALERT_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=YELLOW_ALERT_PING, embed=embed)


async def orange_alert(interaction: discord.Interaction):
    embed = Embed(
        title=ORANGE_ALERT_TITLE,
        description=ORANGE_ALERT_CONTENT,
        color=ORANGE_ALERT_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=ORANGE_ALERT_PING, embed=embed)


async def red_alert(interaction: discord.Interaction):
    embed = Embed(
        title=RED_ALERT_TITLE,
        description=RED_ALERT_CONTENT,
        color=RED_ALERT_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=RED_ALERT_PING, embed=embed)


async def neutral_alert(interaction: discord.Interaction):
    embed = Embed(
        title=NEUTRAL_ALERT_TITLE,
        description=NEUTRAL_ALERT_CONTENT,
        color=NEUTRAL_ALERT_COLOR,
        footer=EMBED_FOOTER.format(author=interaction.user.display_name),
        timestamp=True
    )
    await interaction.response.send_message(EMBED_LOG, ephemeral=True)
    await interaction.channel.send(content=NEUTRAL_ALERT_PING, embed=embed)
