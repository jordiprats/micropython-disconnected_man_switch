from config import wifi_config

import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

import utime
print('sleep 10')
utime.sleep(10)

import uping

while True:
    total_recv = 0
    for i in range(10):
    (n_trans, n_recv) = uping.ping('8.8.8.8', count=1)
    total_recv += n_recv
    utime.sleep(1)

    if total_recv > 0
        utime.sleep(60)
        continue
    else:
        print('ERROR')