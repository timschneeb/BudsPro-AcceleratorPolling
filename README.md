# Galaxy Buds Pro Accelerator Polling
'Stream' accelerator sensor data from the Samsung Galaxy Buds Pro **(slow!)**

## Requirements

### Windows

On Windows, make sure to install version 0.22 of PyBluez.
The latest version (v0.23) does not work properly and fails to enumerate Bluetooth devices.
```
pip install PyBluez==0.22
```

### Linux

On Linux, you can just go ahead and install the latest version of PyBluez.
```
pip install PyBluez
```

## Usage
```
python3 Accelerator.py 64:03:7F:2E:2B:3A
```
```
x=-3063, y=2887, z=-331; x2=3090, y2=2401, z2=-1219
x=-3063, y=2887, z=-331; x2=3090, y2=2401, z2=-1219
x=-3063, y=2887, z=-331; x2=3082, y2=2361, z2=-1295
x=-3063, y=2887, z=-331; x2=3082, y2=2361, z2=-1295
x=-3063, y=2887, z=-331; x2=3411, y2=2159, z2=-875
x=-3473, y=2207, z=-929; x2=3411, y2=2159, z2=-875
x=-3364, y=2399, z=-778; x2=3131, y2=2337, z2=-1301
x=-3364, y=2399, z=-778; x2=3090, y2=2442, z2=-1153
x=-3336, y=2440, z=-710; x2=3188, y2=2273, z2=-1295
```