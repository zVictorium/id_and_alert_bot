import discord

from utils import Data, HandleID
from settings import *


data = Data(ID_DATA_FILENAME)
handler = HandleID()


async def create_id(interaction: discord.Interaction, name: str, surname: str, birth: str, gender: str):
    name = handler.check_name(name)
    surname = handler.check_name(surname)
    birth = handler.check_date(birth)
    gender = handler.check_gender(gender)
    message = None
    embed = None
    if not name or not surname:
        message = WRONG_NAME
    elif not birth:
        message = WRONG_BIRTH
    elif not gender:
        message = WRONG_GENDER
    else:
        valid_id = None
        while not valid_id:
            id = handler.generate_id()
            valid_id = handler.check_id(id, data.get_values())
        id_data = {
            NAME: name,
            SURNAME: surname,
            BIRTH: birth,
            GENDER: gender,
            ID: id
        }
        data.add_value(interaction.user.id, id_data)
        embed = handler.get_embed_id(interaction.user, id_data)
    await interaction.response.send_message(content=message, embed=embed, ephemeral=True)


async def show_id(interaction: discord.Interaction, user: discord.User):
    if not user:
        user = interaction.user
    user_id = user.id
    id = data.get_value(user_id)
    message = None
    embed = None
    if id:
        embed = handler.get_embed_id(user, id)
        ephemeral = False
    else:
        message = MISSING_ID
        ephemeral = True
    await interaction.response.send_message(content=message, embed=embed, ephemeral=ephemeral)


async def edit_id(interaction: discord.Interaction, user: discord.User, name: str, surname: str, birth: str, gender: str):
    user_id = user.id
    message = None
    embed = None
    if str(user_id) in data.get_keys():
        if name or surname or birth or gender:
            id_data = data.get_value(user_id)
            if name:
                name = handler.check_name(name)
                if name:
                    id_data[NAME] = name
                else:
                    message = WRONG_NAME
            if surname:
                surname = handler.check_name(surname)
                if surname:
                    id_data[SURNAME] = surname
                else:
                    message = WRONG_NAME
            if birth:
                birth = handler.check_date(birth)
                if birth:
                    id_data[BIRTH] = birth
                else:
                    message = WRONG_BIRTH
            if gender:
                gender = handler.check_gender(gender)
                if gender:
                    id_data[GENDER] = gender
                else:
                    message = WRONG_GENDER
            data.add_value(user_id, id_data)
            embed = handler.get_embed_id(interaction.user, id_data)
        else:
            message = EDIT_FAIL
    else:
        message = MISSING_USER_ID
    await interaction.response.send_message(content=message, embed=embed, ephemeral=True)


async def remove_id(interaction: discord.Interaction, user: discord.User):
    user_id = user.id
    if str(user_id) in data.get_keys():
        data.remove_value(user_id)
        message = ID_REMOVED
    else:
        message = MISSING_USER_ID
    await interaction.response.send_message(message, ephemeral=True)


async def help_id(interaction: discord.Interaction):
    await interaction.response.send_message(content=ID_HELP, ephemeral=True)