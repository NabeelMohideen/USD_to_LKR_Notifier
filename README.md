# USD_to_LKR_DiscordBot

## USD_to_LKR_DiscordBot_V1.0
This script fetches the latest USD to LKR currency rate and sends it to Discord via a webhook. It saves the rate into a variable. It checks for rate changes every 15 minutes and, if detected, triggers an alert with the current date and time.

```sh
$ python USD_to_LKR_DiscordBot_V1.0.py
```

Discord Alert Structure

```
@everyone
USD to LKR Bot Notify Every Change v2.0
Date: 15-01-2024
Time: 13:34:36
USD to LKR Rate: 321.71
```

## USD_to_LKR_DiscordBot_V2.0
This script fetches the latest USD to LKR currency rate and sends it to Discord via a webhook. It checks for rate changes every 15 minutes and, if detected, triggers an alert with the current date and time. The script updates the last_rate.txt file with the latest currency rate.

```sh
$ python USD_to_LKR_DiscordBot_V2.0.py
```

Discord Alert Structure

```
@everyone
USD to LKR Bot Notify Every Change v2.0
Date: 15-01-2024
Time: 13:34:36
USD to LKR Rate: 321.71
```