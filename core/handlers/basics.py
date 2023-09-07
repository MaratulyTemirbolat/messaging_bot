# Python
from typing import Any

# Aiogram
from aiogram import Bot
from aiogram.types import Message

# Project
from core.api.services import (
    handle_get,
    HOST_NAME,
)


async def handle_start_command(
    message: Message,
    bot: Bot,
    *args: tuple[Any],
    **kwargs: dict[Any, Any]
) -> None:
    """Handle START command function."""
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Привет <b>{message.from_user.first_name}</b>. "
        "Рад тебя видеть в нашем чате\r\n",
    )


async def handle_text(
    message: Message,
    bot: Bot,
    *args: tuple[Any],
    **kwargs: dict[Any, Any]
) -> None:
    """Handle all messages from the user."""
    if message.text:
        response: dict[str, Any] = await handle_get(
            url=f"{HOST_NAME}/api/v1/auths/users/telegram_connect",
            headers={
                "Authorization": f"JWT {message.text}"
            },
            params={
                "chat_id": message.from_user.id
            },
        )
        if response["status"] // 100 == 2:
            print("Success")
            await message.answer(
                text="Ваш токен успешно принят!\n" +
                     response['response']['detail']
            )
        elif response["status"] >= 400:
            print("error")
            await message.answer(
                text=f"Произошла ошибка! {response['response']['detail']}"
            )
    else:
        await message.answer(
            text="Извините, но я могу принимать только текст"
        )


async def handle_unclear_request(
    message: Message,
    *args: tuple[Any],
    **kwargs: dict[Any, Any]
) -> None:
    """Handle unclear requests."""
    await message.answer(
        text="Извините, но я могу принимать только текст сообщений"
    )
