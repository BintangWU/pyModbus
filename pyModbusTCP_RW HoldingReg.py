from datetime import datetime, time
from pymodbus.client import ModbusTcpClient
import random
import time
import json


def currentTime():
    now = datetime.now().isoformat()
    return now

client = ModbusTcpClient(host='192.168.250.10', port=502)
while True:

    client.connect()
    newValue = random.randint(10, 90);
    readValue = client.read_holding_registers(20, 10)
    client.write_register(29, newValue)

    data = {
        "dateTime": currentTime(),
        "data": readValue.registers
    }

    print("\n")
    print(json.dumps(data))
    time.sleep(2)
