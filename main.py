import RPi.GPIO as GPIO
import FSR_402
import HC_SR04
import GPS
import Emergency

GPIO.setwarnings(False)
button = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
latitude, longitude = GPS.GPS()

GPS.GPS_result()
print(latitude, longitude)

while True:
    distance = HC_SR04.distance()
    Left = FSR_402.cha0()
    Right = FSR_402.cha1()
    Center = FSR_402.cha2()
    Back = FSR_402.cha3()
    Front = FSR_402.cha4()
    inputIO = GPIO.input(button)
    
    if inputIO == False:
        Emergency.SOS()
        print("sos")

    else :
        if Center + Left + Right + Front + Back > 1500:
            FSR_402.cha_result()
            GPS.GPS_result()
            HC_SR04.distance_result()
            print("Distance => ", distance, "cm")
            print("Center : ",Center, ",Left : ",Left, ",Right : ",Right, ",Front : ",Front, ",Back : ",Back)
            print("total : ", Center+Left+Right+Front+Back)

        elif Center or Left or Right or Front or Back > 0:
            FSR_402.cha_result()
            HC_SR04.distance_result()
            print("Distance => ", distance, "cm")
            print("Center : ",Center, ",Left : ",Left, ",Right : ",Right, ",Front : ",Front, ",Back : ",Back)
            print("total : ", Center+Left+Right+Front+Back)
        
