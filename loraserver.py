import requests
import json

class Loraserver:
    """
    Basic interaction with Loraserver RESTful API.
    """

    def __init__(self, base_url, jwt):
        self.base_url = base_url
        self.jwt = jwt

    def get_jwt(self, user, password):
        pass

    def authenticate(self, user, password):
        pass

    def create_device(self, applicationID, description, devEUI, deviceProfileID, name, skipFCntCheck, referenceAltitude=0):
        data = {
            "device": {
                "applicationID": applicationID,
                "description": description,
                "devEUI": devEUI,
                "deviceProfileID": deviceProfileID,
                "name": name,
                "referenceAltitude": referenceAltitude,
                "skipFCntCheck": skipFCntCheck
            }
        }

        return self.__post("/api/devices", data)

    def delete_device(self, id):
        pass

    def get_applications(self):
        pass
    
    def get_device_profiles(self):
        pass

    def __post(self, endpoint, data):

        headers = {
            'Content-Type': "application/json",
            'Grpc-Metadata-Authorization': f"Bearer {self.jwt}"
        }

        url = self.base_url + endpoint

        response = requests.post(url, data=json.dumps(data), headers=headers)

        return response.text

    def __get(self, *args):
        pass

if __name__ == "__main__":
    
    url = 'http://iot.smartcityfrb.dk:8080'
    jwt = 'xx'
    
    ls = Loraserver(url, jwt)

    res = ls.create_device('2', 'Python test fra classe', 'e444429134949491', 'de80034f-313c-477e-b6cd-4f11fe63d36e', 'python_test', True, 0)

    print(res)
