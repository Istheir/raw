import network
import machine
 
# 存储WiFi参数到非易失性存储
def save_wifi_config(ssid, password):
    with open('wifi_config.txt', 'w') as f:
        f.write('ssid=' + ssid + '\n')
        f.write('password=' + password + '\n')
 
# 读取WiFi参数从非易失性存储
def load_wifi_config():
    ssid = None
    password = None
    try:
        with open('wifi_config.txt', 'r') as f:
            for line in f:
                if line.startswith('ssid='):
                    ssid = line.strip()[len('ssid='):]
                elif line.startswith('password='):
                    password = line.strip()[len('password='):]
    except OSError:
        # 文件不存在或其他错误
        pass
    return ssid, password
 
# 连接到WiFi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            print('...')
            time.sleep(1)
    print('Connected to WiFi:', wlan.ifconfig())
 
# 使用示例
# 读取WiFi参数
ssid, password = load_wifi_config()
 
# 如果WiFi参数已存储，则连接到WiFi
if ssid and password:
    connect_to_wifi(ssid, password)
 
# 你可以根据需要修改save_wifi_config和load_wifi_config函数，使用不同的文件名或存储方式。
