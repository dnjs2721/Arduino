def API(): #API.txt의 각 열을 lines배열에 입력하는 모듈 / lines[0] = IP, lines[1] = Port
    file_path = "/home/pi/Arduino/API.txt" 
    with open(file_path) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines
            
def shock(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 충격센서
    lines = API()
    shock_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sensor/shockSensor'
    return shock_URL

def wearing(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 거리센서
    lines = API()
    wearing_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sensor/wearing'
    return wearing_URL

def gps(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 거리센서
    lines = API()
    gps_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sensor/gps'
    return gps_URL

def sos(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 버튼
    lines = API()
    sos_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sensor/sos'
    return sos_URL