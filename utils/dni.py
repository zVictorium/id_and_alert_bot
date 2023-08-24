import random
import string
from datetime import datetime
from settings import *
from utils import Embed


class IDHandler():

    def check_name(self, name: str):
        contain_spaces = ' ' in name
        name = name.capitalize()
        name = None if contain_spaces else name
        return name

    def check_date(self, date: str):
        try:
            date = datetime.strptime(date, '%d-%m-%Y')
            date = f'{date.day}-{date.month}-{date.year}'
            return date
        except ValueError:
            return None

    def check_gender(self, gender: str):
        gender = gender.capitalize()
        for valid_gender in VALID_GENDERS:
            if gender.lower() == valid_gender.lower():
                return gender
        return None

    def generate_id(self):
        numbers = ''.join(str(random.randint(0, 9)) for _ in range(8))
        character = random.choice(string.ascii_uppercase)
        id = f'{numbers}{character}'
        return id

    def check_id(self, id: str, values):
        for id_data in values:
            if id == id_data[ID]:
                return False
        return True

    def id_message(self, mention: str, id: dict):
        message = DNI_MESSAGE.format(
            user=mention,
            name=id[NAME],
            surname=id[SURNAME],
            birth=id[BIRTH],
            gender=id[GENDER],
            id=id[ID]
        )
        return message

    def id_embed(self, mention: str, id: dict):
        fields = [
            ('**Nombre:**', f'`{id[NAME]}`', True),
            ('**Apellido:**', f'`{id[SURNAME]}`', True),
            ('**Nacimiento:**', f'`{id[BIRTH]}`', True),
            ('**Género:**', f'`{id[GENDER]}`', True),
            ('**DNI:**', f'`{id[ID]}`', True)
        ]
        embed = Embed(
            title=f'__**DNI de {id[NAME]} {id[SURNAME]}**__',
            fields=fields
        )
        return embed
