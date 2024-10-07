from machine import Timer
 
count = 10
 
def on_timer(timer):
    global count
    if count > 0:
        print(f"倒计时: {count}秒")
        count -= 1
    else:
        print("倒计时结束!")
        timer.deinit()  # 停止计时器
 
# 创建一个定时器，并设置回调函数on_timer
timer = Timer(0)
timer.init(period=1000, mode=Timer.PERIODIC, callback=on_timer)
