import discord
from utils import Embed
from settings import *

async def poll(interaction: discord.Interaction):
    embed = Embed(title=POLL_TITLE, description=POLL_DESCRIPTION, color=POLL_COLOR)
    await interaction.response.send_message(embed=embed, ephemeral=False)


async def server_open(interaction: discord.Interaction):
    embed = Embed(title=SERVER_OPEN_TITLE, description=SERVER_OPEN_DESCRIPTION, color=SERVER_OPEN_COLOR)
    await interaction.response.send_message(embed=embed, ephemeral=False)


async def reset(interaction: discord.Interaction):
    embed = Embed(title=RESET_TITLE, description=RESET_DESCRIPTION, color=RESET_COLOR)
    await interaction.response.send_message(embed=embed, ephemeral=False)


async def server_close(interaction: discord.Interaction):
    embed = Embed(title=SERVER_CLOSE_TITLE, description=SERVER_CLOSE_DESCRIPTION, color=SERVER_CLOSE_COLOR)
    await interaction.response.send_message(embed=embed, ephemeral=False)


async def maintenance(interaction: discord.Interaction):
    embed = Embed(title=MAINTENANCE_TITLE, description=MAINTENANCE_DESCRIPTION, color=MAINTENANCE_COLOR)
    await interaction.response.send_message(embed=embed, ephemeral=False)
