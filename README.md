Home assistant monkey patches
=============================

Example custom_component to monkey patch a library.

~~The example includes a monkey patch for from `async_upnp_client.aiohttp.AiohttpSessionRequester.async_http_request` from [async_upnp_client](https://github.com/StevenLooman/async_upnp_client).~~

This version enables Home assistant to handle a Denon Ceol Piccolo device per DLNA even though the device seems to raise an UpnpXmlParseError when not in Media Server Mode.
It patches `DlnaDmrEntity.async_update` to not disconnect on UpnpXmlParseError.

enable with
```
monkey_patches:
```
in `configuration.yaml`


you might want to also enable debugmessages by adding:
```
logger:
  default: warning
  logs:
    homeassistant.components.dlna_dmr: debug
    custom_components.monkey_patches: debug
```




This is not supported by me or Home Assistant itself by any means. This is merely meant as an example. Please do not create issues or pull requests.
