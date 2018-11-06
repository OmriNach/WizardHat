from pylsl import StreamInfo, StreamOutlet
import numpy as np
import time
def construct_stream():
    info = StreamInfo('ExperimentName', 'Markers', 1, 1, 'int32','Markers' )
    outlet = StreamOutlet(info)
    marker = [1]
    return outlet, marker
def stream_markers(outlet, marker,duration=23):
    start = time.time()
    while time.time() - start < duration:
        timestamp = time.time()
        outlet.push_sample(marker, timestamp)
        time.sleep(1)


outlet, marker = construct_stream()
stream_markers(outlet, marker)