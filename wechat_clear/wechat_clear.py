#encoding=utf-8
from wxpy import *
import time
import random

bot = Bot()

all_friends = bot.friends()
myself = bot.self

print('----------------BEGIN----------------')

print("检测到你联系人共计: "+ str(len(all_friends)) + " 人")

index = 1;
for user in all_friends:
    time.sleep(random.randint(0,9))
    try:
        if user != myself:
            print("["+str(index)+"/"+str(len(all_friends))+"] "+user.name)
            user.send('能看到我发的吗 జ్ఞా ')
    except ResponseError as e:
        print(e.err_code, e.err_msg) 
    index += 1    

print("检测已执行完毕请到手机微信app中处理")

print('----------------END----------------')   
