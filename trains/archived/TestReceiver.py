from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, ColorDistanceSensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait, StopWatch
from Colours import HSVColor, get_colour
from Channels import Channels


hub = CityHub(
    # broadcast_channel=Hubs.InnerLoopController,
    observe_channels=[Channels.InnerLoopTrain]
)

motor = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B)

loopTimer = StopWatch()
hub.light.on(Color.GREEN)

DEBUG = True

prevReceived = None

while True:
    loopTimer.reset()

    data = hub.ble.observe(Channels.InnerLoopTrain)
    if DEBUG and data is not None and data != prevReceived:
        print("Received", data)
        prevReceived = data

    if data == 0:
        hub.light.on(Color.RED)
        motor.stop()
    elif data == 1:
        hub.light.on(Color.BLUE)
        motor.dc(50)

    got_color = get_colour(sensor)
    if got_color == HSVColor.MEDIUMBLUE:
        motor.dc(30)
    elif got_color == HSVColor.TEAL:
        motor.dc(60)

    wait(50)
    t = loopTimer.time()
    if t > 51:
        print("Loop took", t)
