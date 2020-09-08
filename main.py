from config import wifi_config

debug = True

import machine

pin = machine.Pin(22, machine.Pin.OUT, value=0)

import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan()
sta_if.connect(wifi_config['ssid'], wifi_config['password'])

import utime
print('>> sleep 30 >> waiting for network') if debug
utime.sleep(30)

import uping

try:
    while True:
        total_recv = 0
        for i in range(10):
            (n_trans, n_recv) = uping.ping('1.1.1.1', count=4)
            total_recv += n_recv
            utime.sleep(1)

        if total_recv > 0:
            print('== PING OK ==') if debug if debug
            utime.sleep(60)
            continue
        else:
            print('== ERROR 1.1.1.1, RETRY 8.8.8.8 ==') if debug
            utime.sleep(10)
            total_recv = 0
            for i in range(10):
                (n_trans, n_recv) = uping.ping('8.8.8.8', count=4)
                total_recv += n_recv
                utime.sleep(1)

            if total_recv > 0:
                print('== NOT DEAD ==') if debug
                utime.sleep(30)
                continue
            else:
                print('## 8.8.8.8 not answering') if debug
                raise Exception('DEAD')
except:
    print('>> DEAD <<') if debug

    # RESET ROUTER
    print('>> POWER OFF ROUTER <<') if debug
    pin.on()
    utime.sleep(10)
    print('>> POWER ON ROUTER <<') if debug
    pin.off()
    
    utime.sleep(120)
    machine.reset()