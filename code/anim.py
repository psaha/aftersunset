import numpy as np
import numpy.random as ran
import matplotlib.pyplot as pl

N = 20

nu = np.linspace(0,0.25,N) + 1
a0 = ran.random(N)
b0 = ran.random(N)
z = 0j*np.zeros(2*N)

ha = [0,0]
hb = [0,0]
hm = [0,0]
R = 4*N**.5
for p in range(2):
    pl.subplot(121+p,axisbg='black')
    ax = pl.gca()
    ax.set_aspect('equal')
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ha[p] = pl.plot(a0,a0,lw=3,c='cyan')[0]
    hb[p] = pl.plot(b0,b0,lw=3,c='magenta')[0]
    hm[p] = pl.plot(0,0,'o',markersize=12,c='white')[0]
    pl.xlim(-R,R)
    pl.ylim(-R,R)


for k in range(10000):
    t = 0.02*k
    a = np.exp(2j*np.pi*(nu*t+a0))
    b = np.exp(2j*np.pi*(nu*t+b0))
    b *= 1
    for p in range(2):
        z = np.concatenate(([0],a,(1-2*p)*b))
        for n in range(2*N):
            z[n+1] += z[n]
        ha[p].set_xdata(z.real[:N+1])
        ha[p].set_ydata(z.imag[:N+1])
        hb[p].set_xdata(z.real[N:])
        hb[p].set_ydata(z.imag[N:])
        hm[p].set_xdata(z[-1].real)
        hm[p].set_ydata(z[-1].imag)
    pl.pause(0.04)


