"""Monkey patches for async_upnp_client."""

import logging
import re
from typing import Mapping, Optional, Tuple

from async_upnp_client.aiohttp import AiohttpSessionRequester


_LOGGER = logging.getLogger(__name__)


ROUTER_RE = r"<info>"


async def _async_http_request_patched(
    self,
    method: str,
    url: str,
    headers: Optional[Mapping[str, str]] = None,
    body: Optional[str] = None,
) -> Tuple[int, Mapping[str, str], str]:
    """Apply RE after doing a request."""
    status_code, response_headers, response_body = await self._async_http_request_orig(method, url, headers, body)

    if url == "...":
        response_body = re.sub(ROUTER_RE, "", response_body, flags=re.DOTALL)

    return status_code, response_headers, response_body



AiohttpSessionRequester._async_http_request_orig = AiohttpSessionRequester.async_http_request
AiohttpSessionRequester.async_http_request = _async_http_request_patched
_LOGGER.warn("Monkey patches installed for async_upnp_client installed")
