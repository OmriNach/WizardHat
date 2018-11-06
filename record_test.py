import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire

streamer = ble2lsl.Dummy(muse2016)
receiver = acquire.Receiver.record(10, dejitter=False)

