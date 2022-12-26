from datetime import time, datetime
from pymodbus.client import ModbusTcpClient, AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException
from PyQt5 import QtWidgets, uic
import time, json

class UI(QtWidgets.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('pyModbus.ui', self)

        self._host = ""
        self._port = ""
        self.client = ModbusTcpClient(host=None, port=None)

        self.closeBtn.setEnabled(False)

        # ===== ===== Do some things buttons ===== =====
        self.openBtn.clicked.connect(self.openConnection)
        self.closeBtn.clicked.connect(self.closeConncetion)
        self.clearBtn.clicked.connect(lambda: self.outputTxt.clear())

        # ===== ===== Block RW D register ===== =====
        self.dReadBtn.clicked.connect(self.D_read)
        self.dWriteBtn.clicked.connect(self.D_write)

        # ===== ===== Block RW W register ===== =====
        self.wReadBtn.clicked.connect(self.W_read)
        self.wWriteBtn.clicked.connect(self.W_write)

        self.show()

    def openConnection(self):
        self._host = self.ipTxt.text()
        self._port = self.portTxt.text()
        self.outputTxt.append(f'Connecting... \n{self._host}:{self._port}')

        try:
            self.client = ModbusTcpClient(host=self._host, port=int(self._port))
            statusClient = self.client.connect()
            self.outputTxt.append(f'Connected\n' if statusClient == True else 'Failed || TimeOut\n')
            
            if statusClient:
                self.openBtn.setEnabled(False)
                self.closeBtn.setEnabled(True)
            else:
                self.openBtn.setEnabled(True)
                self.closeBtn.setEnabled(False)

        except:
            self.popUp('Check IP or Port setting!')
            
            self.openBtn.setEnabled(True)
            self.closeBtn.setEnabled(False)

    def closeConncetion(self):
        self.client.close()
        self.outputTxt.append(f'Close connection... \n{self._host}:{self._port}\n')

        print(f'Close connection: {self.client.close()}')

        self.openBtn.setEnabled(True)
        self.closeBtn.setEnabled(False)

    # ===== ===== Block RW D register ===== =====
    def D_read(self):
        _dAddr = self.dAddrTxt.text()

        if self.client.is_socket_open():
            try:
                drVal = self.client.read_holding_registers(address = int(_dAddr), count = 1)
                self.outputTxt.append(f'Read D {_dAddr}\nValue: {drVal.registers}\n')
            except:
                self.popUp('Empty value!')
        else:
            self.popUp('PLC not connected!')
    
    def D_write(self):
        _dAddr = self.dAddrTxt.text()
        _dValue = self.dValTxt.text()

        if self.client.is_socket_open():
            try:
                self.client.write_register(address = int(_dAddr), value = int(_dValue))
                self.outputTxt.append(f'Write D {_dAddr}\nValue: {_dValue}\n')
            except:
                self.popUp('Empty value!')
        else:
            self.popUp('PLC not connected!')

    # ===== ===== Block RW W register ===== =====
    def W_read(self):
        _wAddr = self.wAddrTxt.text()
        _wBit = self.wBitTxt.text()

        temp = self.calcAddr(_wAddr, _wBit)
        #temp = (int(_wAddr) * 16) + int(_wBit)

        if self.client.is_socket_open():
            try:
                wrVal = self.client.read_coils(address = temp, count = 1)
                self.outputTxt.append(f'Read W{_wAddr}.{_wBit}\n{wrVal.bits[0]}\n')
            except:
                self.popUp('Empty value!')
        else:
            self.popUp('PLC not connected!')

    def W_write(self):
        _wAddr = self.wAddrTxt.text()
        _wBit = self.wBitTxt.text()
        _wVal = self.wValTxt.text()

        temp = self.calcAddr(_wAddr, _wBit)

        if self.client.is_socket_open():
            try:
                self.client.write_coils(address=temp, values=[int(_wVal)])
                self.outputTxt.append(f'Write W{_wAddr}.{_wBit}\n{True if int(_wVal) == 1 else False}\n')
            except:
                self.popUp('Empty value!')
        else:
            self.popUp('PLC not connected!')

    # ===== ===== PopUp message function ===== =====
    def popUp(self, msgPopUp):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle('Error!')
        msgBox.setText(msgPopUp)
        msgBox.exec_()

    def calcAddr(self, addr, bit):
        if addr.isnumeric():
            return (int(addr) * 16) + int(bit)
        else:
            self.popUp("value is not numeric")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    uiWindow = UI()
    sys.exit(app.exec_())




