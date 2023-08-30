"""Monkey patches."""

import logging
from homeassistant.core import HomeAssistant

from homeassistant.helpers.typing import ConfigType


_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Keep hass happy."""
    _LOGGER.warn("Installing monkey patches")
    #from . import async_upnp_client
    from . import media_player
    _LOGGER.warn("Monkey patches installed")

    return True
