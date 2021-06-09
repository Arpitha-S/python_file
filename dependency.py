import requests
import json
from datetime import datetime

url = 'http://localhost:8080/api/v2/import-scan/'

headers = {'Authorization': 'Token d7163c979de993065820c094150109a22c0e916f'}

files = {'file': open('https://github.com/Arpitha-S/python_file.git/dependency-check-report.xml','rb')}

dia = datetime.today().strftime('%Y-%m-%d')
print(dia)

body = {'scan_date': dia,
'scan_type': 'Dependency Check Scan',
'engagement': '1',
'lead': '1'
}

r = requests.post(url, headers=headers, files=files, verify=False, data=body)

print("Status Code :%s"%r.status_code)
print("Respuesta :%s"%r.text)
