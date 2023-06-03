import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, -1, -1):
        time.sleep(1)
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) # 格式化时间显示
        print(timer, end="\r") # 打印时间并不换行，使时间在同一行输出
    print("Time's up!")
