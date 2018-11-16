
from multiprocessing import Process
import record_test
import exp


import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire, transform


recording = Process(target=record_test.start())
stimulus = Process(target=exp.start())

recording.start()
stimulus.start()




