# Python
from dataclasses import dataclass

# Third party
from decouple import config


@dataclass
class CustomBot:
    bot_token: str
    admin_id: int


@dataclass
class Setting:
    bot: CustomBot


def get_settings() -> Setting:
    return Setting(
        bot=CustomBot(
            bot_token=config("BOT_TOKEN", cast=str),
            admin_id=config("ADMIN_CHAT_ID", cast=int)
        )
    )


settings: Setting = get_settings()
