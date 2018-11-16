import pylsl as lsl

stream = lsl.resolve_stream()

inlet = lsl.StreamInlet(stream)

data = []
[data, timestamp] = inlet.pull_chunk()
data.append([data, timestamp])
