# Shim per Python 3.13 - discord.py vuole audioop ma non esiste piu'
def __getattr__(name):
    if name == 'ratecv':
        def ratecv(fragment, width, nchannels, inrate, outrate, state, weightA=1, weightB=0):
            return fragment, state
        return ratecv
    if name in ('minmax', 'avg', 'rms', 'avgpp', 'maxpp', 'cross', 'findfactor', 'findfit', 'findmax', 'getsample', 'lin2lin', 'lin2ulaw', 'ulaw2lin', 'lin2alaw', 'alaw2lin', 'lin2adpcm', 'adpcm2lin'):
        def _zero(*args, **kwargs):
            return 0
        return _zero
    def _dummy(fragment, *args, **kwargs):
        if isinstance(fragment, (bytes, bytearray)):
            return bytes(fragment)
        return fragment
    return _dummy

def mul(fragment, width, factor):
    return bytes(fragment)
def tomono(fragment, width, l, r):
    return bytes(fragment)
def tostereo(fragment, width, l, r):
    return bytes(fragment)
def add(f1, f2, width):
    return bytes(f1)
def bias(fragment, width, bias):
    return bytes(fragment)
def reverse(fragment, width):
    return bytes(fragment)
def ratecv(fragment, width, nchannels, inrate, outrate, state, weightA=1, weightB=0):
    return bytes(fragment), state
