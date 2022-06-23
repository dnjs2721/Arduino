import RPi.GPIO as GPIO
import requests, json
import time
import posturl

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

def distance(): #센서의 값을 반환하는 모듈
    GPIO.output(17, False)
    time.sleep(0.1)
    GPIO.output(17, True)
    time.sleep(0.00001)
    GPIO.output(17, False)
   
    while GPIO.input(18) == 0:
        start = time.time()
       
    while GPIO.input(18) == 1:
        stop = time.time()
       
    time_interval = stop - start
    distance = time_interval * 17000
    distance = round(distance, 2)
    return distance

def distance_result(): #센서의 값을 post통신으로 서버에 전송하는 모듈
    a = distance()
    if a < 7 :
        Distance_result = "착용"
    else :
        Distance_result = "미착용"

    data = json.dumps({ #보내는 데이터 : HelmetID와 센서 값(distance)
            'helmetId' : 'H0001',
            'wearingCondition' : Distance_result
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.wearing(), data=data, headers=header) #posturl의 wearing 모듈이 나타내는 서버로 데이터 전송
    return Distance_result


if __name__ == '__main__': #shock_detection.py가 단독으로 실행될때 실행

    while True:
        print("Distance => ", distance(), "cm")
        distance_result()