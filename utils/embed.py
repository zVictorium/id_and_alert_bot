import discord


class Embed(discord.Embed):
    
    def __init__(
        self,
        title: str = '',
        url: str = '',
        description: str = '',
        color: str = 'ffffff',
        author_name: str = '',
        author_url: str = '',
        author_icon_url: str = '',
        icon_url: str = '',
        fields: list = [],
        footer: str = ''
    ):
        super().__init__(
            title=title,
            url=url,
            description=description,
            color=int(color, 16)
        )

        if author_name:
            self.set_author(
                name=author_name,
                url=author_url,
                icon_url=author_icon_url
            )

        if icon_url:
            self.set_thumbnail(url=icon_url)

        if fields:
            for name, value, inline in fields:
                self.add_field(name=name, value=value, inline=inline)

        if footer:
            self.set_footer(text=footer)