from typing import Callable
from typing import List

from custom_components.argoclima.const import DOMAIN
from custom_components.argoclima.device_type import InvalidOperationError
from custom_components.argoclima.entity import ArgoEntity
from homeassistant.components.number import NumberEntity
from homeassistant.components.number import NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_devices: Callable[[List[NumberEntity]], None],
):
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_devices([ArgoEcoLimitNumber(coordinator, entry)])


class ArgoEcoLimitNumber(ArgoEntity, NumberEntity):
    def __init__(self, coordinator, entry: ConfigEntry):
        ArgoEntity.__init__(
            self,
            "Eco Mode Power Limit",
            coordinator,
            entry,
            None,
            EntityCategory.CONFIG,
        )
        NumberEntity.__init__(self)

    @property
    def icon(self) -> str:
        return "mdi:leaf"

    @property
    def value(self) -> float:
        if not self._type.eco_limit:
            raise InvalidOperationError
        return self.coordinator.data.eco_limit

    @property
    def min_value(self) -> int:
        if not self._type.eco_limit:
            raise InvalidOperationError
        return self._type.eco_limit_min

    @property
    def max_value(self) -> int:
        if not self._type.eco_limit:
            raise InvalidOperationError
        return self._type.eco_limit_max

    @property
    def step(self) -> int:
        if not self._type.eco_limit:
            raise InvalidOperationError
        return 1

    @property
    def mode(self) -> NumberMode:
        return NumberMode.BOX

    async def async_set_value(self, value: float) -> None:
        if not self._type.eco_limit:
            raise InvalidOperationError
        self.coordinator.data.eco_limit = int(value)
        await self.coordinator.async_request_refresh()
