# Python
from typing import Any

# aiogram
from aiogram import Bot
from aiogram.types import (
    BotCommand,
    BotCommandScopeDefault,
)


async def set_commands(
    bot: Bot,
    *args: tuple[Any],
    **kwargs: dict[Any, Any]
) -> None:
    """Set all the commands for bot working."""
    commands: list[BotCommand] = [
        BotCommand(
            command="start",
            description="Запустить бота"
        ),
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )
