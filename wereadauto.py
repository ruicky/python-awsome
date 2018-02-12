import wda
import time
import datetime

c = wda.Client()

s = c.session()
# print s.orientation

def main():
    s.tap(350,400) # 根据手机型号自行修改触发位置

if __name__ == '__main__':
    startTime = datetime.datetime.now();
    while 1:
        nowTime = datetime.datetime.now();
        mkt_last = time.mktime(startTime.timetuple());
        mkt_now = time.mktime(nowTime.timetuple());
        delt_time = (mkt_now-mkt_last)/60   #转成分钟
        # 5小时 ＝＝＝ 300分钟
        leftTime = 300 - delt_time ;
        if leftTime > 0 :
            # print("剩余" + str(int(leftTime)) + '分钟');
            print("已读书" + str(int(delt_time)) + '分钟');
            time.sleep(10)
            main();
        else:
            print("自动读书完毕");
            break;    