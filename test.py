from loraserver import Device, LoraServerClient
from csv_helper import read_csv

user = "xx"
password = "xx"
url = 'http://iot.smartcityfrb.dk:8080/api'
ls = LoraServerClient(url, user, password)


devices = read_csv("test.csv")

data = [Device(dev[0], dev[1], dev[2], dev[3], dev[4], True, 0) for dev in devices]

#create devices
# for item in data:
#     print(ls.create_device(item))

# delete devices
for item in data:
    print(ls.delete_device(item.devEUI))


#dev1 = Device('2', 'Python test fra classe we', 'e111129134249491', 'de80034f-313c-477e-b6cd-4f11fe63d36e', 'python_test', True, 0)


