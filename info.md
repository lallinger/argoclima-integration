![Project Status][project-status-shield]
[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

## Supported devices and features

At the moment, only the device I own is supported. There is a good chance that other wifi capable devices use the same API thoug. So if you own a different device, please feel
| Feature | Implementation / Supported for | Ulisse 13 DCI Eco WiFi |
| ---------------------------- | ------------------------------ | ---------------------- |
| on / off | `climate` operation | ✓ |
| operation mode | `climate` operation | ✓ |
| eco mode | `climate` preset | ✓ |
| turbo mode | `climate` preset | ✓ |
| night mode | `climate` preset | ✓ |
| current temperature | `climate` | ✓ |
| set target temperature | `climate` | ✓ |
| set fan speed | `climate` fan mode | ✓ |
| set flap mode | x | - |
| set filter mode | x | - |
| set active timer | `select` | ✓ |
| use remote temperature | `switch` | ✓ |
| timer configuration | x | x |
| set current time and weekday | set_time service | ✓ |
| device lights on / off | `switch` | ✓ |
| display unit \* | `select` | ✓ |
| eco mode power limit | `number` | ✓ |
| firmware version \*\* | device registry | ✓ |
| reset device | x | x |

[`text`] _platform the feature is represented by in HA_\
[-] _not supported by the device_\
[x] _not implemented_

\* This only affects the value displayed on the device and the webinterface.
\*\* Not visible in the frontend.

{% if not installed %}

## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Argoclima".

{% endif %}

## Adding your device to Home Assistant

At the moment, the integration will communicate with the device locally. Cloud based communication is not supported.

### Set up WiFi

Follow the instructions provided with the device to connect it to your network. Once that is done, I highly recommend assigning it a static IP via router configuration. The integration is IP based and can not identify the device by any other means.

### Configuration

Select your device type, give it a name and enter the IP. The IP can be changed later.\
![configuration](https://raw.githubusercontent.com/nyffchanium/argoclima-integration/master/config.png)

## Using the Remote Sensor

The temperature sensor integrated in the remote can still be used.\
To make this work:

1. To not overwrite the device's configuration, e.g. cover up the IR diode of the remote.
2. Set the state of the remote to On (indicated by e.g. the grid lines and the fan icon being visible).
3. Enable remote temperature mode (indicated by the user icon, toggled by holding the fan button for 2 seconds). _This might not be required. Not sure._

If my observations are correct, the remote will now send the temperature (no other settings):

- every 6 minutes if no change is detected
- whenever the temperature displayed on the remote changes

Probably more often, but that's what I found.

## Restrictions / Problems

- If an API request is sent while another one is still in progress, the latter will be cancelled. It does not matter whether any of the requests actually changes anything. I.e. concerning parallel requests, only the most recent one is regarded by the device.\
  Because of this, you should not use the official wep app in addition to this integration.
- In case a value could not be changed (due to the problem mentioned above), it will be sent again until it is confirmed.
- Because the response of an update request does not contain the updated information, updates will be sent twice in most cases.
- There are however settings that can only be written and thus there is no way to check if they have been accepted. This affects current time and weekday, timer configuration and reset. Those values will only be sent once.

## Troubleshooting

**Device can't be created / Device is unavailable, the IP is correct and the device is connected:**\
Turn off the device and unplug it, leave it for _an unknown amount of time (1min is enough for sure)_, then try again.

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter][cookie_cutter] template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template.

---

[argoclima]: https://github.com/nyffchanium/argoclima-integration
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[project-status-shield]: https://img.shields.io/badge/project%20status-released-brightgreen.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/nyffchanium
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/nyffchanium/argoclima-integration.svg?style=for-the-badge
[commits]: https://github.com/nyffchanium/argoclima-integration/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Default-brightgreen.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license]: https://github.com/nyffchanium/argoclima-integration/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/nyffchanium/argoclima-integration.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40nyffchanium-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/nyffchanium/argoclima-integration.svg?style=for-the-badge
[releases]: https://github.com/nyffchanium/argoclima-integration/releases
[user_profile]: https://github.com/nyffchanium
[cookie_cutter]: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component
[integration_blueprint]: https://github.com/custom-components/integration_blueprint
