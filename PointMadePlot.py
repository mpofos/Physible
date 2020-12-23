import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d

n = len(sys.argv[1])
a = sys.argv[1][1:n-1]
X = a.split(',')

X = [float(i) for i in X]


n = len(sys.argv[2])
a = sys.argv[2][1:n-1]
Y = a.split(',')

Y = [float(i) for i in Y]

x = np.array(X)
y = np.array(Y)
# y = 2x
plt.grid(True)
m, b = np.polyfit(X, Y, 1)
xnew = np.linspace(0, 10, num=41, endpoint=True)
plt.plot(X, Y, 'o')
plt.plot(x, m*x + b,'--')
plt.legend(['Actual Points', 'Calculated Plot'], loc='best')
plt.show()
