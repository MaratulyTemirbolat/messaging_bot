# Python
from typing import Any

# Third party
from aiohttp import ClientSession
from aiohttp.client_exceptions import (
    ServerDisconnectedError,
    ClientConnectorError,
)

# Project
from core.api.http_statuses import HTTP_503_SEERVICE_UNAVAILABLE

HOST_NAME = "http://temirbwd.beget.tech"

UNAVAILABLE_SERVER_RESPONSE = {
    "status": HTTP_503_SEERVICE_UNAVAILABLE,
    "response": {
        "detail": "Извините, не удается установить соединение с сервером"
    }
}

SERVER_DISCTONNECTED_RESPONSE = {
    "status": HTTP_503_SEERVICE_UNAVAILABLE,
    "response": {
        "deetail": "Извините, но сервер сейчас недоступен"
    }
}


async def handle_get(
    url: str,
    headers: dict[str, Any] = {},
    params: dict[str, Any] = {},
    *args: tuple[Any],
    **kwargs: dict[Any, Any]
) -> dict[str, Any]:
    result_response: dict[str, Any] = {}
    try:
        async with ClientSession(headers=headers) as session:
            async with session.get(
                url=url,
                ssl=False,
                params=params
            ) as response:
                result_response.setdefault("status", response.status)
                result_response.setdefault("response", await response.json())
        return result_response
    except ServerDisconnectedError:
        return SERVER_DISCTONNECTED_RESPONSE
    except ClientConnectorError:
        return UNAVAILABLE_SERVER_RESPONSE
