import math
import numpy as np
import matplotlib.pyplot as plt

y = []
z = []
prop = []
Lambda = []
t = []

sigma = 1.0/4.5
beta = sigma*2.25
theta = 0.14 
N = 66870000.0
rho = 0.001
psi = 17

y.append(1.0/N)
z.append(0.0)
prop.append(1.0)
Lambda.append(0.0)
t.append(0.0)

dt = 1.0

for i in range(1,77):
  y.append(y[i-1] + (beta*y[i-1]*(1.0 - z[i-1]) - sigma*y[i-1]))
  z.append(z[i-1] + (beta*y[i-1]*(1.0 - z[i-1])))
  prop.append(1.0 - z[i])
  if i - psi < 0:
    Lambda.append(Lambda[i-1])
  if i - psi >= 0:
    Lambda.append(N*rho*theta*z[i-psi])
  t.append(t[i-1] + dt)

  print t[i], y[i], z[i], Lambda[i]

y2 = []
z2 = []
prop2 = []
Lambda2 = []
t2 = []

sigma2 = 1.0/4.5
beta2 = sigma*2.25
theta2 = 0.14
N2 = 66870000.0
rho2 = 0.01
psi2 = 17

y2.append(1.0/N)
z2.append(0.0)
prop2.append(1.0)
Lambda2.append(0.0)
t2.append(9.0)

dt = 1.0

for i in range(1,67):
  y2.append(y2[i-1] + (beta2*y2[i-1]*(1.0 - z2[i-1]) - sigma2*y2[i-1]))
  z2.append(z2[i-1] + (beta2*y2[i-1]*(1.0 - z2[i-1])))
  prop2.append(1.0 - z2[i])
  if i - psi2 < 0:
    Lambda2.append(Lambda2[i-1])
  if i - psi2 >= 0:
    Lambda2.append(N2*rho2*theta2*z2[i-psi2])
  t2.append(t2[i-1] + dt)

  print t2[i], y2[i], z2[i], Lambda2[i]

y3 = []
z3 = []
prop3 = []
Lambda3 = []
t3 = []

sigma3 = 1.0/4.5
beta3 = sigma*2.25
theta3 = 0.14
N3 = 66870000.0
rho3 = 0.1
psi3 = 17

y3.append(1.0/N)
z3.append(0.0)
prop3.append(1.0)
Lambda3.append(0.0)
t3.append(19.0)

dt = 1.0

for i in range(1,58):
  y3.append(y3[i-1] + (beta3*y3[i-1]*(1.0 - z3[i-1]) - sigma3*y3[i-1]))
  z3.append(z3[i-1] + (beta3*y3[i-1]*(1.0 - z3[i-1])))
  prop3.append(1.0 - z3[i])
  if i - psi3 < 0:
    Lambda3.append(Lambda3[i-1])
  if i - psi3 >= 0:
    Lambda3.append(N3*rho3*theta3*z3[i-psi3])
  t3.append(t3[i-1] + dt)

  print t3[i], y3[i], z3[i], Lambda3[i]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Time (days)')
ax1.set_ylabel('Proportion susceptible')
#ax1.set_yscale('log')
ax1.plot(t, prop, color='red',label='$\\rho = 0.001$')
ax1.plot(t2, prop2, color='black',ls='dashed',label='$\\rho = 0.01$')
ax1.plot(t3, prop3, color='blue', ls='dotted',label='$\\rho = 0.1$')

ax1.legend(loc='lower left')

ax2 = ax1.twinx()

ax2.set_ylabel('Cumulative deaths')
ax2.set_yscale('log')
ax2.set_ylim(1.0,600.0)
ax2.plot(t, Lambda, color='red')
ax2.plot(t2, Lambda2, color='black',ls='dashed')
ax2.plot(t3, Lambda3, color='blue',ls='dotted')

fig.tight_layout()

plt.savefig('transmission_1.png')
plt.show()

