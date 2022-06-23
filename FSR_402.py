import spidev
import time
import requests, json
import posturl 

Vcc = 5.0
R1 = 1000
# SPI 활성화
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# FSR-402 값 계산
def fsr420_Registor(voltage):
    R = (R1 * Vcc)/voltage - R1
    return R
 
# ADC 채널 분류
def ReadChannel(channel):
    adc = spi.xfer([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def cha(Num):
    index = 0
    analog_level = ReadChannel(Num)
    Vout = analog_level * Vcc / 1024.0
    if(Vout < 2.2):
        Vout = 0.001
        Rfsr = 5000000
        analog_level = 0
    else:
        Rfsr = fsr420_Registor(Vout)
        index += 1
    return analog_level

def cha_result(): #센서의 값을 post통신으로 서버에 전송하는 모듈
    Left_result = cha(0) 
    Right_result = cha(1)
    Center_result = cha(2) 
    Back_result = cha(3)
    Front_result = cha(4)
    data = json.dumps({
            'helmetId' : 'H0001',
            'shockDataLeft' : Left_result,
            'shockDataRight' : Right_result,
            'shockDataCenter' : Center_result,
            'shockDataBack' : Back_result,
            'shockDataFront' : Front_result
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.shock(), data=data, headers=header) #해당 API의 서버로 데이터를 전송

if __name__ == '__main__':
    while True :
        Left = cha(0)
        Right = cha(1)
        Center = cha(2)
        Back = cha(3)
        Front = cha(4)
        if Center or Left or Right or Front or Back > 0:
            print("Center : ",Center, ",Left : ",Left, ",Right : ",Right, ",Front : ",Front, ",Back : ",Back)
            print("total : ", Center+Left+Right+Front+Back)
            cha_result()
        time.sleep(0.03)
   