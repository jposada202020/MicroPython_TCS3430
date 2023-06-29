# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_tcs3430 import tcs3430

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
tcs = tcs3430.TCS3430(i2c)

tcs.als_operation_mode = tcs3430.ALS_DISABLED

while True:
    for als_operation_mode in tcs3430.als_operation_mode_values:
        print("Current Als operation mode setting: ", tcs.als_operation_mode)
        for _ in range(10):
            lux = tcs.lux
            print("Temperature: {:.2f}g".format(lux))
            print()
            time.sleep(0.5)
        tcs.als_operation_mode = als_operation_mode
