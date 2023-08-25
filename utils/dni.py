import random
import string
from datetime import datetime

from settings import *
from utils import Embed


class HandleID():

    def check_name(self, name: str):
        contain_spaces = ' ' in name
        name = name.capitalize()
        name = None if contain_spaces else name
        return name

    def check_date(self, date: str):
        try:
            date = datetime.strptime(date, '%d/%m/%Y')
            date = f'{date.day}/{date.month}/{date.year}'
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

    def get_embed_id(self, user, id: dict):
        fields = [
            (ID_MESSAGE_FULLNAME, f'{id[NAME]} {id[SURNAME]}', False),
            (ID_MESSAGE_GENDER, id[GENDER], False),
            (ID_MESSAGE_BIRTH, id[BIRTH], False),
            (ID_MESSAGE_ID, id[ID], False)
        ]
        embed = Embed(
            title=ID_MESSAGE_TITLE.format(name=id[NAME], surname=id[SURNAME]),
            fields=fields,
            author_name=ID_MESSAGE_AUTHOR.format(username=user.display_name),
            author_icon_url=user.avatar.url,
            icon_url=user.avatar.url,
            timestamp=True
        )
        return embed
