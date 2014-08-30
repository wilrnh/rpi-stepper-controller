#!/usr/bin/env python
from RPIO import PWM

PWM.setup()
PWM.init_channel(0, 1000000)

PWM.add_channel_pulse(0, 17, 0, 1400)

while True:
  pass

