from BluetoothService import BluetoothService
from RepeatedTimer import RepeatedTimer

import struct


class AcceleratorSensorManager:
    def __init__(self, socket, data_callback, verbose=False, debug=False):
        # Constants
        self.MSG_DEBUG_GET_ALL_DATA = 38

        # Member variables
        self.data_cb = data_callback
        self.verbose = verbose
        self.service = BluetoothService(socket, self.__onMessageReceived, debug)
        self.timer = None

    def attach(self):
        self.timer = RepeatedTimer(0.5, self.__poll)

    def detach(self):
        self.timer.stop()

    def __poll(self):
        self.service.sendPacket(self.MSG_DEBUG_GET_ALL_DATA, bytes())

    def __onMessageReceived(self, data):
        if data[3] == self.MSG_DEBUG_GET_ALL_DATA:
            left = struct.unpack('{}h'.format(3), data[4 + 18:4 + 24])
            right = struct.unpack('{}h'.format(3), data[4 + 24:4 + 30])

            if self.data_cb is not None:
                self.data_cb(left, right)

