import socket
import machine
import time
import network

SSID="yanfa5"
PASSWORD="kuncai6888"
port=80
wlan=None
listenSocket=None

def connectWifi(ssid,passwd): #建立wifi连接
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  return True

#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head>
<title>MicroPython IoT longer</title>
<style>
body {background-color: white}
h1 {color:red}

button {
        color: red;
        height: 200px;
        width: 200px;
        background:white;
        border: 3px solid #4CAF50; /* Green */
        border-radius: 50%;
        font-size: 250%;
        position: center;
}
</style>
</head>
<body>
<center><h1>Botdemy IoT Car Control</h1>
<form>
<div><button name="CMD" value="up" type="submit">Forward</button></div>
<div><button name="CMD" value="Ti" type="submit">Left</button>
<button name="CMD" value="stop" type="submit">Stop</button>
<button name="CMD" value="Si" type="submit">Right</button></div>
<div><button name="CMD" value="down" type="submit">Back</button></div>
</form>
</center>
</body>
</html>
"""

#steup
pin12 = machine.Pin(12, machine.Pin.OUT) #方向
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.OUT) #开关
pin13.value(0)
global pwn_freq
pwn_freq = 10000
pwm15 = machine.PWM(machine.Pin(15))
pwm15.duty(256)
pwm15.freq(pwn_freq)
global time_up
time_up = 36.5

def up():
    pin12.value(1)
    time.sleep_ms(100)
    pin13.value(1)
    time.sleep_ms(100)

def down():
    pin12.value(0)
    time.sleep_ms(100)
    pin13.value(1)
    time.sleep_ms(100)

def stop():
    pin13.value(0)
    time.sleep_ms(100)

def si():
    print('执行Si')
    time_up = 36.5
    pwm15.freq(10000)
    down()
    print('下降')
    print(time_up)
    time.sleep(time_up)
    stop()
    pwm15.freq(4500)
    time_up = 82
    up()
    print('上升')
    print(time_up)
    time.sleep(time_up)
    stop()
    time_up = 240
    print('停止')
    print(time_up)
    time.sleep(time_up)
    time_up = 36.5
    pwm15.freq(10000)
    down()
    print('下降')
    print(time_up)
    time.sleep(time_up)
    stop()
    pwm15.freq(4500)
    time_up = 82
    up()
    print('上升')
    print(time_up)
    time.sleep(time_up)
    stop()
    print('停止')

def ti():
    print('执行TI')
    time_up = 36.5
    pwm15.freq(10000)
    down()
    print('下降')
    print(time_up)
    time.sleep(time_up)
    stop()
    pwm15.freq(2200)
    time_up = 165
    up()
    print('上升')
    print(time_up)
    time.sleep(time_up)
    stop()
    time_up = 60
    print('停止')
    print(time_up)
    time.sleep(time_up)
    time_up = 36.5
    pwm15.freq(10000)
    down()
    print('下降')
    print(time_up)
    time.sleep(time_up)
    stop()
    pwm15.freq(2200)
    time_up = 165
    up()
    print('上升')
    print(time_up)
    time.sleep(time_up)
    stop()
    print('停止')



#Setup Socket Web
connectWifi(SSID,PASSWORD)
ip=wlan.ifconfig()[0]

listenSocket = socket.socket() #建立一个实例
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listenSocket.bind((ip,port))  #绑定建立网路连接的ip地址和端口
listenSocket.listen(5) #开始侦听

print ('tcp waiting...')

while True:
    print("accepting.....")
    conn, addr = listenSocket.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)

    CMD_up = request.find('/?CMD=up') #如果在请求的包中，发现有/?CMD=forward，下同
    CMD_down = request.find('/?CMD=down')
    CMD_Ti = request.find('/?CMD=Ti')
    CMD_Si = request.find('/?CMD=Si')
    CMD_stop = request.find('/?CMD=stop')

    print("Data: " + str(CMD_up))
    print("Data: " + str(CMD_down))
    print("Data: " + str(CMD_Ti))
    print("Data: " + str(CMD_Si))
    print("Data: " + str(CMD_stop))

    if CMD_up == 6: #如果此命令有效，下同
        print('+up')
        pwm15.freq(10000)
        up()
        time.sleep(1)
    if CMD_down == 6:
        print('+down')
        pwm15.freq(10000)
        down()
        time.sleep(1)
    if CMD_TI == 6:
        print('+left')
        pwm15.freq(10000)
        ti()
    if CMD_Ti == 6:
        print('+Si')
        si()
    if CMD_stop == 6:
        print('+stop')
        pwm15.freq(0)
        stop()
    response = html #将html的网页定义装载在回应字段
    conn.send(response) #send到浏览器上，就形成了控制界面
    conn.close()
