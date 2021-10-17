#!/usr/bin/env python3

"""
A python script to stream head-tracking data from the Samsung Galaxy Buds Pro
"""

# License: MIT
# Author: @ThePBone
# 04/26/2021
import time

import bluetooth
import sys
import argparse

from AcceleratorSensorManager import AcceleratorSensorManager


def __accelerator_sensor_callback(left, right):
    # Each parameter is a float list containing the raw xyz values of the accelerometer
    # The values are ordered like this: x, y, z
    print(f"x={left[0]}, y={left[1]}, z={left[2]}; x2={right[0]}, y2={right[1]}, z2={right[2]}")


def main():
    parser = argparse.ArgumentParser(description='Stream accelerator data from the Galaxy Buds Pro (slow)')
    parser.add_argument('mac', metavar='mac-address', type=str, nargs=1,
                        help='MAC-Address of your Buds')
    parser.add_argument('-v', '--verbose', action='store_true', help="Print debug information")
    parser.add_argument('-t', '--trace', action='store_true', help="Trace Bluetooth serial traffic")
    args = parser.parse_args()

    verbose = args.verbose
    trace = args.trace

    if verbose:
        print(str(bluetooth.lookup_name(args.mac[0])))
        print("Searching for RFCOMM interface...")

    service_matches = bluetooth.find_service(uuid="00001101-0000-1000-8000-00805F9B34FB", address=str(args.mac[0]))

    port = host = None
    for match in service_matches:
        if match["name"] == "GEARMANAGER" or match["name"] == b"GEARMANAGER":
            port = match["port"]
            host = match["host"]
            break

    if port is None or host is None:
        print("Couldn't find the proprietary RFCOMM service")
        sys.exit(1)

    if verbose:
        print("RFCOMM interface found. Establishing connection...")

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))

    if verbose:
        print("Connected to device.")

    sensor = None
    try:
        sensor = AcceleratorSensorManager(sock, __accelerator_sensor_callback, verbose, trace)
        sensor.attach()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        if sensor is not None:
            sensor.detach()


if __name__ == "__main__":
    main()
