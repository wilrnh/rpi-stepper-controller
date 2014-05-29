#!/bin/sh
pause=0.001
#gpio -g mode 23 out
rpio --setoutput 23
#gpio -g mode 24 out
rpio --setoutput 24


for i in $(seq 30); do

echo round $i starts:
sleep 1

#gpio -g write 24 1
rpio -s 24:1
for i in $(seq 3600); do
  echo $i
  #gpio -g write 23 1
  rpio -s 23:1
  sleep $pause
  #gpio -g write 23 0
  rpio -s 23:0
  sleep $pause
done
sleep 1
#gpio -g write 24 0
rpio -s 24:0
for i in $(seq 200); do
  echo $i
  #gpio -g write 23 1
  rpio -s 23:1
  sleep $pause
  #gpio -g write 23 0
  rpio -s 23:0
  sleep $pause
done
done
