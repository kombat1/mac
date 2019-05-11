import xml.etree.ElementTree as ET
import requests
import sys

try:
	mac = sys.argv[1].replace('-','')
except:
	pass	
data = requests.get('https://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks='+mac+':-65&app=ymetro')
xml = ET.fromstring(data.text)
try:
	print(xml.find('./coordinates').attrib['latitude'])
	print(xml.find('./coordinates').attrib['longitude'])
except:
	print('Erorr to MAC')	