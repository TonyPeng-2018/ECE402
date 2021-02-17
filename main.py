# This file is for RP board to control the switcher
# The switcher has a VDD from 2.5 to 4.8, so we chosse VDD=3.3V
# The control voltage low is from 0 to 0.4
# The control voltage high is from 1.335 to 2.7, so we set port to 1.8 V
# This file need a input which allow us to use switcher
# The control current should be about or more than 50 mA.
# However, GPIO provide no more than 16 mA current, it is a problem
# Import GPIO module to control the RP board
# Port information https://juejin.cn/post/6868946182325043207. also here https://learnku.com/articles/42701
import RPi.GPIO as GPIO
import sys
# Set GPIO mode, we use port 11 to control, initial Low.
# port 11 -> control 1; port 13 -> control 2; port 15 -> control 3
RPi.GPIO.setmode(GPIO.BOARD)
# 3 ports high, the switch shut down
GPIO.setup(11, GPIO.OUT, initial=GPIO.High)
GPIO.setup(13, GPIO.OUT, initial=GPIO.High)
GPIO.setup(15, GPIO.OUT, initial=GPIO.High)
HL_control = input("Which RF do you need to connect?")

# Use HL_control to control the ports
HL_control_list = [1,2,3,4,5]
if HL_control not in HL_control_list:
    sys.exit()
GPIO.output(11, HL_control in [2])
GPIO.output(13, False)
GPIO.output(15, HL_control in [3])

# Shut down the switcher first
HL_control = input("input anything to end")
GPIO.output(11, True)
GPIO.output(13, True)
GPIO.output(15, True)
sys.exit()