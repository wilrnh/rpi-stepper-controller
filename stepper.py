#!/usr/bin/python
import RPIO
import time

RPIO.setup(23,RPIO.OUT)
RPIO.setup(24,RPIO.OUT)

pause=1
step_cnt=1600
rounds=30

for i in range(rounds):
  print "Round %s starts" % i

  time.sleep(1.0)
  RPIO.output(24, True)

  for s in range(step_cnt):
    print s
    RPIO.output(23,True)
    time.sleep(pause)
    RPIO.output(23,False)
    time.sleep(pause)

  time.sleep(1.0)
  RPIO.output(24, False)

  for s in range(step_cnt):
    print s
    RPIO.output(23,True)
    time.sleep(pause)
    RPIO.output(23,False)
    time.sleep(pause)

