"""Monkey patches for async_update_patched."""

import logging
import re
from typing import Mapping, Optional, Tuple

from homeassistant.components.dlna_dmr.media_player import DlnaDmrEntity
from async_upnp_client.exceptions import UpnpXmlParseError, UpnpError, UpnpResponseError

_LOGGER = logging.getLogger(__name__)


# Original here: https://github.com/home-assistant/core/blob/867e9b73bbcad4f681f8996833d65690b4765527/homeassistant/components/dlna_dmr/media_player.py#L417
async def async_update_patched(self) -> None:
        """Retrieve the latest data."""
        if not self._device:
            if not self.poll_availability:
                return
            try:
                await self._device_connect(self.location)
            except UpnpError:
                return

        assert self._device is not None

        try:
            do_ping = self.poll_availability or self.check_available
            await self._device.async_update(do_ping=do_ping)
        except UpnpXmlParseError as err:
            #Device seems to send bad XML. So does Denon Ceol Piccolo when not in Media Server mode
            _LOGGER.debug("Device NOT unavailable: %r", err)
            return
        except UpnpError as err:
            _LOGGER.debug("Device unavailable: %r", err)
            await self._device_disconnect()
            return
        finally:
            self.check_available = False

DlnaDmrEntity._async_update_orig = DlnaDmrEntity.async_update
DlnaDmrEntity.async_update=async_update_patched
_LOGGER.warn("Monkey patches installed for async_update installed")
