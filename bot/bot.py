import requests
import json
import time

headers = {"content-type": "application/json"}

data = {
	"instances": [
		[1.03203516, -0.00805019, -1.2978844, 0.88989014, 0.43414292,
			-0.50806998, 0.40460721, -0.19109181, 0.46569821, 0.28164328,
			-1.62740851, -0.91137128, -2.20009422, 0.94312013, -0.30184054,
			-0.53605743, -0.24712953, -0.22079268, -0.02329695, -0.41743359,
			0.01712106, 0.0752892, -0.0191709, 0.69969526, 0.87391227,
			-1.04943005, -0.10138927, -0.17668808, 0.34269317
		]
	]

}

json_data = json.dumps(data)

while True:
    response = requests.post('http://creditfraud-service:8501/v1/models/creditfraud:predict', data=json_data, headers=headers)

    if response.status_code == 200:
        predictions = response.json()
        print(predictions)
    
    time.sleep(0.01)
