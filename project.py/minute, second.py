import datetime
now = datetime.datetime.now()
separated_second= []
separated_minute= []
# 시간과 분 받기
second = now.strftime('%S')
minute = now.strftime('%M')

second_1= int(int(second)/10)
second_2= int(int(second)%10)

minute_1= int(int(minute)/10)
minute_2= int(int(minute)%10)




