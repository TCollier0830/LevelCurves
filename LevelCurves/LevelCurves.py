from matplotlib.pyplot import cm
from numpy import *
import matplotlib.pyplot as plt

def max_min(inputlist):
    return max([max(sublist) for sublist in inputlist]), min([min(sublist) for sublist in inputlist])

T1 = 0
T2 = 100

fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 

#Radius = linspace(0,1,50)
#Complex = exp(linspace(0,pi,50)*1j)
#rad, com = meshgrid(Radius,Complex)
#z = rad*com

Real = linspace(-pi/2,pi/2,500)
Complex = linspace(0,4,500)*1j
r, c = meshgrid(Real,Complex)
z = r + c
cc = abs(cos(z.real)/sinh(z.imag))

#h = ((T2-T1)/(2*pi))*(angle((1 + sin(z))/(sin(z)-1))) + T1
h = ((T2-T1)/(2*pi))*log(cc)
#h = (T2-T1)/2*(angle((1 + sin(z))/(sin(z)-1))) + T1
max,min = max_min(h)
boi = linspace(min,max,2000)
cs = plt.contour(z.real,z.imag,h,levels = boi)
bar = fig.colorbar(cs)
ax.set_title('Lines of Flow')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim([-pi/1.9,pi/1.9])
ax.set_ylim([-.1, 4.1])
#plt.show()
plt.savefig('LinesOfFlow3.png', dpi = 300)