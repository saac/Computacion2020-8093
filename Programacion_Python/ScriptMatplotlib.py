import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc

rc('text', usetex=True)

x = np.linspace(-np.pi,np.pi)
fx = np.cos(x)
fx1 = np.sin(x)

plt.figure(figsize=(7,7))

plt.plot(x, fx, color='olive', ls='-', lw=2, label='$\cos(x)$')
plt.plot(x,fx1,color='#a41b81',marker='.',ms=9,ls='None',label='$\sin(x)$')

plt.title("Funciones periodicas",fontsize=20)
plt.xlabel("$x$",fontsize=18)
plt.ylabel("$f(x)$",fontsize=18)
plt.legend(loc=2)

plt.grid(True)
plt.text(-np.pi/2, -1.1, 'Minimo',horizontalalignment='center',
         verticalalignment='baseline')
plt.annotate('Maximo',(np.pi/2,1),xytext=(2.5,0.9),
             arrowprops=dict(facecolor='black',width=1,headwidth=5,shrink=0.05),
             horizontalalignment='left')

plt.xlim(-np.pi,np.pi)

yt = np.arange(-1,1.5,0.5)
plt.yticks(yt,fontsize=18)
xt = [-np.pi,0,np.pi]
xt_labels = ['$-\pi$','$0$' ,'$\pi$']
plt.xticks(xt,xt_labels,fontsize=18)


# plt.savefig('FPeridocas.pdf')
plt.show()
