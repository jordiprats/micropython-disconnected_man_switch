# micropython-disconnected_mans_switch

### Disconnected man's switch

By connecting this between the power line of your main router, it will reset it in case you no longer have internet access

### config.py

WiFi config is set using the **config.py** file, you can use the **config.py-demo** as a template

```
wifi_config = {
    'ssid':'DEMO',
    'password':'PASSW0RD'
}
```

## Connections

| ESP32  | RELAY |
|--------|-------|
| V5     | VCC  |
| GND    | GND  |
| GPIO22 | IN   |


## uPing

* [shawwwn](https://gist.github.com/shawwwn/91cc8979e33e82af6d99ec34c38195fb)
