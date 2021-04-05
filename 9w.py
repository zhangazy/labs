import matplotlib.pyplot as plt 
import numpy as np 
def fun(x):
    if x < 0:
        return 0
    else:
        return x+2
def an(n):
    n = int(n)
    if(n%2 != 0):
        return (-2)/(n**2)
    else:
        return 0 
def bn(n):
    n = int(n)
    if(n%2 == 0):
        return(-np.pi)/(np.pi*n)
    else:
        return (4+np.pi)/(np.pi*n)
def fourierSeries (m, x):
    a0 = (np.pi/4) + 1
    partialSums = a0
    for n in range(1, m):
        try:
            partialSums = partialSums + an(n)*np.cos(n*x) + bn(n) * np.sin(n*x)
        except:
            print("pass")
            pass
    return partialSums
x_ = np.linespace(-np.pi, np.pi, 100)
y = []
f = []
for i in x_:
    y.append(fun(i))
    f.append(fourierSeries(5, i))

plt.plot(x_, y, color = "blue", label = "Function")
plt.plot(x_, f, color = "red", label = "Fourier series approximation with m = 5")
pplt.show()

y= []
f= []
for i in x_:
    y.append(fun(i))
    f.append(fourierSeries(5, i))

plt.plot(x_, y, color="blue" , label= "Function")
plt.plot(x_, f, color="red", label= "Fourier series approximate with m=5")
plt.legend()
plt.show()

y= []
f= []
for i in x_:
    y.append(fun(i))
    f.append(fourierSeries(20, i))

plt.plot(x_, y, color="blue" , label= "Function")
plt.plot(x_, f, color="red", label= "Fourier series approximate with m=5")
plt.legend()
plt.show()