import requests
import json

class Loraserver:
    """
    Basic interaction with Loraserver RESTful API.
    """

    def __init__(self, base_url, jwt):
        self.base_url = base_url
        self.jwt = jwt
        self.headers = {
            'Content-Type': "application/json",
            'Grpc-Metadata-Authorization': f"Bearer {self.jwt}"
        }

    def get_jwt(self, user, password):
        pass

    def authenticate(self, user, password):
        pass

    def post(self, endpoint, data):

        url = self.base_url + endpoint

        response = requests.post(url, data=json.dumps(data), headers=self.headers)

        return response.text

    def get(self, endpoint):
        pass

    def delete(self, endpoint):
        
        url = self.base_url + endpoint
        
        print(url)

        response = requests.delete(url, headers=self.headers)

        return response.text


class Device(Loraserver):

    endpoint = "/api/devices"

    def create(self, applicationID, description, devEUI, deviceProfileID, name, skipFCntCheck, referenceAltitude=0):
        """
        creates the given device.
        """
        
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

        return self.post(self.endpoint, data)

    def delete_device(self, dev_eui):
        """
        Delete deletes the device matching the given DevEUI.
        """

        url = f"{self.endpoint}/{dev_eui}"

        return self.delete(url)


class DeviceProfile(Loraserver):

    def get_device_profiles(self):
        pass


class Application(Loraserver):

    def get_applications(self):
        pass


if __name__ == "__main__":
    
    url = 'http://iot.smartcityfrb.dk:8080'
    jwt = '..--'
    
    dev = Device(url, jwt)

    #res = dev.create('2', 'Python test fra classe', 'e144429134249491', 'de80034f-313c-477e-b6cd-4f11fe63d36e', 'python_test3', True, 0)
    res = dev.delete_device('e444489994949499')
    print(res)
