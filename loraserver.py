import requests
import json

class LoraServerClient:
    """
    Basic interaction with Loraserver RESTful API.
    """

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.jwt = self.get_jwt_token(self.user, self.password)
        self.headers = {
            'Content-Type': "application/json",
            'Grpc-Metadata-Authorization': f"Bearer {self.jwt}"
        }

    def create_device(self, device):
        """
        creates the given device, from device object
        """
        data = {
            "device": device.__dict__
        }

        return self.__post("/devices", data)

    def updata_device(self):
        pass

    def delete_device(self, dev_eui):
        """
        Delete deletes the device matching the given DevEUI.
        """

        url = f"/devices/{dev_eui}"

        return self.__delete(url)

    def add_device_keys(self, device, keys):
        pass

    def get_jwt_token(self, username, password):
        """
        Fetch JWT token using user and password from Loraserver app.
        """
        data = {
            "username": self.user,
            "password": self.password
        }
        url = self.base_url + "/internal/login"
        response = requests.post(url, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()["jwt"]
        else:
            raise Exception(response.text)

    def __post(self, endpoint, data):

        url = self.base_url + endpoint
        response = requests.post(url, data=json.dumps(data), headers=self.headers)

        return response.text, response.status_code

    def __get(self, endpoint):
        pass

    def __delete(self, endpoint):
        
        url = self.base_url + endpoint
        response = requests.delete(url, headers=self.headers)

        return response.text, response.status_code


class Device:
    """
    Data class for devices fx. used when creating devices
    """
    def __init__(self, applicationID, description, devEUI, deviceProfileID, name, skipFCntCheck, referenceAltitude=0):
        self.applicationID = applicationID
        self.description = description
        self.devEUI = devEUI
        self.deviceProfileID = deviceProfileID
        self.name = name
        self.referenceAltitude = referenceAltitude
        self.skipFCntCheck = skipFCntCheck