from pyo import *
import time

s = Server().boot()
s.start()
f = Fader(fadein=0.5, fadeout=0.5, dur=2, mul=.5)
a = BrownNoise(mul=f).mix(2).out()
def repeat():
  f.play()
pat = Pattern(function=repeat, time=2).play()
time.sleep(3)