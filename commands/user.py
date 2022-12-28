from datetime import datetime, timezone

from disinter.api import DiscordAPI
from disinter.components import Embed, EmbedField, EmbedThumbnail
from disinter.context import SlashContext


def UserCommand(ctx: SlashContext, api: DiscordAPI):
    userid = ctx.options["userid"]["value"]

    try:
        user = api.get_user(userid)

        user_avatar = user["avatar"]
        avatar = ""
        if user_avatar is None:
            avatar = f"https://cdn.discordapp.com/embed/avatars/{int(user['discriminator']) % 5}.png"
        else:
            avatar = f"https://cdn.discordapp.com/avatars/{user['id']}/{user_avatar}.png?size=1024"

        print(avatar)

        timestamp = (int(user["id"]) >> 22) + 1420070400000

        embed = Embed(
            title=f"{user['username']}'s Profile",
            description="User information",
            timestamp=datetime.now(timezone.utc).isoformat(),
            fields=[
                EmbedField(name="ID", value=f"{user['id']}", inline=True),
                EmbedField(name="Username", value=f"{user['username']}", inline=True),
                EmbedField(
                    name="Member Since",
                    value=f"{datetime.utcfromtimestamp(timestamp/1000.0).strftime('%b %d, %Y')}",
                ),
            ],
            thumbnail=EmbedThumbnail(url=avatar),
        )

        return ctx.reply(embeds=[embed])

    except Exception as e:
        embed = Embed(
            title="Error",
            description=f"There was a problem while trying to get the user.\n```{str(e)}```",
            timestamp=datetime.now(timezone.utc).isoformat(),
        )

        return ctx.reply(embeds=[embed])
