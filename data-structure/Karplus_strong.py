import numpy as np
import random, wave
from collections import deque

def generateNote(freq):
    nSamples = 44100
    sampleRate = 44100
    N =int(sampleRate/freq)
    buf = deque([random.random() - 0.5 
                                for i in range(N)])
    samples = np.array([0]*nSamples, 'float32')
    for i in range(nSamples):
        samples[i] =buf[0]
        avg = 0.995 *0.5 *(buf[0]+buf[1])
        buf.append(avg)
        buf.popleft()
    samples = np.array(samples * 32767, 'init16')
    return samples.tostring()

    def writeWAVE(fname, data):
        file = wave.open(fname, 'wb')
        nChannels = 1
        
    
    