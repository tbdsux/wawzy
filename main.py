import os

from disinter import DisInter
from disinter.command import (ApplicationCommandOption,
                              ApplicationCommandOptionTypeNumber)
from disinter.context import SlashContext
from dotenv import load_dotenv

from commands import user

# load .env
load_dotenv()


TOKEN = os.environ.get("TOKEN", "")
APPLICATION_ID = os.environ.get("APPLICATION_ID", "")
GUILDS = os.environ.get("GUILD", "").split(",")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY", "")


app = DisInter(
    token=TOKEN, application_id=APPLICATION_ID, guilds=GUILDS, public_key=PUBLIC_KEY
)


@app.slash_command(name="ping", description="Ping the bot.")
def ping(ctx: SlashContext):
    return ctx.reply("Pong!")


@app.slash_command(
    name="user",
    description="View user info with id",
    options=[
        ApplicationCommandOption(
            name="userid",
            type=ApplicationCommandOptionTypeNumber,
            description="The user's id",
            required=True,
        )
    ],
)
def user_command(ctx: SlashContext):
    return user.UserCommand(ctx, app.api)
