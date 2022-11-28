from datetime import datetime, time
from pymodbus.client import ModbusTcpClient
import random
import time
import json

def currentTime():
    now = datetime.now().isoformat()
    return now

client = ModbusTcpClient(host='192.168.250.10', port=502)
value = []

while True:
    client.connect()

    rawResult = client.read_coils(0, 16)
    #client.write_coils(100, [1,1,1,1])
    print(rawResult.bits)
    time.sleep(2)