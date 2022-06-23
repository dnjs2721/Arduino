import subprocess
import requests, json
import posturl


def GPS():
    command = ['gpspipe','-r','-x','4']
    fd_popen = subprocess.Popen(command, stdout=subprocess.PIPE).stdout
    data = fd_popen.read().strip()
    fd_popen.close()
    data = str(data)
    data= data[data.find('GPRMC'):]
    latitude=float(data[18:20])+round(float(data[20:27])/60,6)
    longitude=float(data[30:33])+round(float(data[33:40])/60,6)
    return latitude, longitude

def GPS_result():
    latitude, longitude = GPS()
    data = json.dumps({ 
            'helmetId' : 'H0001',
            'latitude' : latitude,
	        'longitude' : longitude
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.gps(), data=data, headers=header)

if __name__ == '__main__':
    while True :
        latitude, longitude = GPS()
        GPS_result()
        print(latitude,",",longitude)