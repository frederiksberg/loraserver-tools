import requests
import json

class LoraServerClient:
    """
    Basic interaction with Loraserver RESTful API.
    """
    device_endpoint = "/api/devices"

    def __init__(self, base_url, jwt):
        self.base_url = base_url
        self.jwt = jwt
        self.headers = {
            'Content-Type': "application/json",
            'Grpc-Metadata-Authorization': f"Bearer {self.jwt}"
        }

    def create_device(self, device):
        """
        creates the given device, from device object
        """

        return self.__post(self.device_endpoint, device.to_dict())

    def delete_device(self, dev_eui):
        """
        Delete deletes the device matching the given DevEUI.
        """

        url = f"{self.device_endpoint}/{dev_eui}"

        return self.__delete(url)

    def __post(self, endpoint, data):

        url = self.base_url + endpoint

        response = requests.post(url, data=json.dumps(data), headers=self.headers)

        return response.text

    def __get(self, endpoint):
        pass

    def __delete(self, endpoint):
        
        url = self.base_url + endpoint

        response = requests.delete(url, headers=self.headers)

        return response.text


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

    def to_dict(self):

        d = {
            "device": {
                "applicationID": self.applicationID,
                "description": self.description,
                "devEUI": self.devEUI,
                "deviceProfileID": self.deviceProfileID,
                "name": self.name,
                "referenceAltitude": self.referenceAltitude,
                "skipFCntCheck": self.skipFCntCheck
            }
        }

        return d