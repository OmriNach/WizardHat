import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire, transform

    
streamer = ble2lsl.Dummy(muse2016)
receiver = acquire.Receiver.record(10)


#timestamps = receiver.buffers['EEG'].get_timestamps()
#dejittered = acquire.dejitter_timestamps(timestamps,256)
#aligned = transform.Markers(receiver.buffers['EEG'],receiver.buffers['Markers'],dejittered)
