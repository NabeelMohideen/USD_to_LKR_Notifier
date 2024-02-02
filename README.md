# USD_to_LKR_DiscordBot

## USD_to_LKR_DiscordBot_V1.0
This script fetches the latest currency rate and sends it to Discord via a webhook. It then saves the rate to a variable, checking for changes every 15 minutes. If a change is detected, an alert is sent, updating the variable with the latest rate.

```sh
$ python USD_to_LKR_DiscordBot_V1.0.py
```

## USD_to_LKR_DiscordBot_V2.0
This script fetches the latest currency rate and sends it to Discord via a webhook. It saves the current rate to a last_rate.txt file, checking for changes every 15 minutes. If a change is detected, an alert is sent, updating the last_rate.txt file with the latest currency rate.

```sh
$ python USD_to_LKR_DiscordBot_V2.0.py
```