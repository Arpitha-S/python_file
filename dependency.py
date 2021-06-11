import requests
import json
from datetime import datetime

url = 'http://localhost:8080/api/v2/import-scan/'

headers = {'Authorization': 'Token 8cbb86997405cdf9241ad60e87c0d741cd4ff89c ' ,'username': 'admin' 'password': 'p@ssw0rd'}
files = {'file': open('https://github.com/Arpitha-S/python_file.git/dependency-check-report.xml','rb')}

dia = datetime.today().strftime('%Y-%m-%d')
print(dia)

body = {'scan_date': dia,
'scan_type': 'Dependency Check Scan',
'engagement': '10',
'lead': '1'
}

r = requests.post(url, headers=headers, files=files, verify=False, data=body)

print("Status Code :%s"%r.status_code)
print("Respuesta :%s"%r.text)
