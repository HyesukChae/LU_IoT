import time
import RPi.GPIO as GPIO

# ----------------------------------
MOTOR_L_PWM = 12
MOTOR_L_DIR = 5
MOTOR_R_PWM = 13
MOTOR_R_DIR = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # BCM pin number
GPIO.setup(MOTOR_L_PWM,GPIO.OUT) # Left moter PWM
GPIO.setup(MOTOR_L_DIR,GPIO.OUT) # Left motor direction
GPIO.setup(MOTOR_R_PWM,GPIO.OUT) # Right moter PWM
GPIO.setup(MOTOR_R_DIR,GPIO.OUT) # Right moter direction
MOTOR_L = GPIO.PWM(MOTOR_L_PWM,500) # L motor PWM frequency 500Hz
MOTOR_R = GPIO.PWM(MOTOR_R_PWM,500) # R motor PWM frequency 500Hz
MOTOR_L.start(0) # L motor PWM value starts from 0 
MOTOR_R.start(0) # R motor PWM value starts from 0 
# Motor Run Function ------------------------------------------------------
def motorRun(leftMotor, rightMotor):
    
    if leftMotor >= 0:
        GPIO.output(MOTOR_L_DIR,GPIO.HIGH) # L motor forward
    else:
        GPIO.output(MOTOR_L_DIR,GPIO.LOW) # L motor backward
    if rightMotor >= 0:
        GPIO.output(MOTOR_R_DIR,GPIO.HIGH) # R motor forward
    else:
        GPIO.output(MOTOR_R_DIR,GPIO.LOW) # R motor backward
        
    MOTOR_L.ChangeDutyCycle(abs(leftMotor)) # left motor PWM
    MOTOR_R.ChangeDutyCycle(abs(rightMotor)) # right motor PWM
#--------------------------------------------------------------------------
motorRun(70, 70); time.sleep(1) # forward
motorRun(-70, 100); time.sleep(1) # turn left
motorRun(100, -70); time.sleep(1) # turn right
motorRun(-70, -70); time.sleep(1) # backward
motorRun(0, 0) # stop

GPIO.cleanup() # release reserved GPIO module resource 
#==========================================================================
