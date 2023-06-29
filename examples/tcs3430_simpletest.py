# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_tcs3430 import tcs3430

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
tcs = tcs3430.TCS3430(i2c)

while True:
    print(tcs.measurements)
    time.sleep(0.5)
