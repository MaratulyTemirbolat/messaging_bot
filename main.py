# Python
from logging import (
    basicConfig,
    INFO,
)
from typing import (
    Tuple,
    Dict,
    Any,
)

# Third part
from asyncio import run

# Aiogram
from aiogram import (
    Bot,
    Dispatcher,
    F,
)
from aiogram.filters import CommandStart

# Project
from core.handlers.basics import (
    handle_start_command,
    handle_text,
    handle_unclear_request,
)
from core.utils.commands import set_commands
from core.settings import settings


async def start_bot(
    bot: Bot,
    *args: Tuple[Any],
    **kwargs: Dict[Any, Any]
) -> None:
    await set_commands(bot=bot)
    await bot.send_message(
        chat_id=settings.bot.admin_id,
        text="Бот успешно запущен!"
    )


async def stop_bot(
    bot: Bot,
    *args: Tuple[Any],
    **kwargs: Dict[Any, Any]
) -> None:
    await bot.send_message(
        chat_id=settings.bot.admin_id,
        text="Бот остановился!"
    )


async def start() -> None:
    basicConfig(
        level=INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s -"
               "(%(filename)s). %(funcName)s(%(lineno)d) - %(message)s"
    )
    bot: Bot = Bot(
        token=settings.bot.bot_token,
        parse_mode="HTML"
    )

    dp: Dispatcher = Dispatcher()

    # Main system registers
    dp.startup.register(callback=start_bot)
    dp.shutdown.register(callback=stop_bot)

    # Message registrations
    dp.message.register(
        handle_start_command,
        CommandStart()
    )
    dp.message.register(
        handle_text,
        F.text.strip()
    )

    # Unclear requests handler
    dp.message.register(
        handle_unclear_request
    )

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    run(start())
