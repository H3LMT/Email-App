import numpy

key = ""
numpy.save("sg.npy",key)

print(numpy.load("sg.npy"))