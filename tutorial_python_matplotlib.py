# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:26:46 2016

@author: sharath
"""

import numpy as np
import matplotlib.pyplot as plt



X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)



# Simple plot, no customization, good for a quick preview of what the variable
# contents are
plt.plot(C)
plt.plot(S)
plt.show()



# Customizations - figure size, grid
plt.figure(figsize=(6, 4))
plt.plot(X, C)
plt.plot(X, S)
plt.grid()
plt.show()



# Axes limits
plt.figure(figsize=(6, 4))
plt.plot(X, C)
plt.plot(X, S)
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)
plt.grid()
plt.show()



# Linestyles, linewidth, color
plt.figure(figsize=(6, 4))
plt.plot(X, C, linestyle='-', linewidth=2, color='blue')
plt.plot(X, S, linestyle='--', linewidth=3, color='black')
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)
plt.grid()
plt.show()



# x,y ticks
plt.figure(figsize=(6, 4))
plt.plot(X, C, linestyle='-', linewidth=2, color='blue')
plt.plot(X, S, linestyle='--', linewidth=3, color='black')
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)
plt.grid()
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1.0, 0, 1.0])
plt.show()



# Axes and tick labels
plt.figure(figsize=(6, 4))
plt.plot(X, C, linestyle='-', linewidth=2, color='blue')
plt.plot(X, S, linestyle='--', linewidth=3, color='black')
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)
plt.grid()
plt.xlabel('Radians (x)')
plt.ylabel('f(x)')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1.0, 0, 1.0], [r'$-1$', r'$0$', r'$+1$'])
plt.show()



# Legend
plt.figure(figsize=(6, 4))
plt.plot(X, C, linestyle='-', linewidth=2, color='blue', label='cos(x)')
plt.plot(X, S, linestyle='--', linewidth=3, color='black', label='sin(x)')
plt.xlim(-3.5, 3.5)
plt.ylim(-1.25, 1.25)
plt.grid()
plt.xlabel('Radians (x)')
plt.ylabel('f(x)')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1.0, 0, 1.0], [r'$-1$', r'$0$', r'$+1$'])
plt.legend(loc='upper left', frameon=True)
plt.show()



# Scatter plot
np.random.seed(0)
r_u_x = np.random.uniform(size=500)
r_u_y = np.random.uniform(size=500)
plt.scatter(r_u_x, r_u_y)
plt.show()



# Scatter plot - marker size, color, marker style
np.random.seed(0)
plt.figure(figsize=(6, 6))
r_u_x = np.random.uniform(size=500)
r_u_y = np.random.uniform(size=500)
plt.scatter(r_u_x, r_u_y, s=50, c='blue', marker='o', alpha=0.2)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.xticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel(r'$P(x)$')
plt.ylabel(r'$P(y)$')
plt.show()



# Scatter plot - color variation
plt.figure(figsize=(6, 6))
r_u_x = np.random.uniform(size=500)
r_u_y = np.random.uniform(size=500)
clr = np.sqrt(r_u_x**2 + r_u_y**2)
plt.scatter(r_u_x, r_u_y, s=50, c=clr, marker='o', alpha=0.4, cmap=plt.cm.Blues)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.xticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel(r'$P(x)$')
plt.ylabel(r'$P(y)$')
plt.show()



# Scatter plot - color variation
plt.figure(figsize=(6, 6))
r_u_x = np.random.normal(size=2000)
r_u_y = np.random.normal(size=2000)
clr = np.sqrt(r_u_x**2 + r_u_y**2)
plt.scatter(r_u_x, r_u_y, s=20, c=clr, marker='o', alpha=0.6)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.xticks([-4, -2, 0, 2, 4], [r'$-4$', r'$-2$', r'$0$', r'$2$', r'$4$'])
plt.yticks([-4, -2, 0, 2, 4], [r'$-4$', r'$-2$', r'$0$', r'$2$', r'$4$'])
plt.xlabel(r'$P(x)$')
plt.ylabel(r'$P(y)$')
plt.show()



# Bar graph
x = np.arange(7)
y = np.random.uniform(size=7)
plt.figure(figsize=(6, 5))
plt.bar(x+0.1, y)
plt.ylim(0, 1.15)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], [r'$Mon$', r'$Tue$', r'$Wed$', r'$Thurs$', r'$Fri$', r'$Sat$', r'$Sun$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel('Day')
plt.ylabel('P(rain)')
plt.show()



# Bar graph - Line graph
x = np.arange(7)
y = np.random.uniform(size=7)
plt.figure(figsize=(6, 5))
plt.bar(x+0.1, y)
plt.plot(x+0.5, y, color='g', linestyle='--', marker='o')
plt.ylim(0, 1.15)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], [r'$Mon$', r'$Tue$', r'$Wed$', r'$Thurs$', r'$Fri$', r'$Sat$', r'$Sun$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel('Day')
plt.ylabel('P(rain)')
plt.show()



# Bar graph - Adding text
x = np.arange(7)
y = np.random.uniform(size=7)
plt.figure(figsize=(6, 5))
plt.bar(x+0.1, y)
plt.ylim(0, 1.15)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], [r'$Mon$', r'$Tue$', r'$Wed$', r'$Thurs$', r'$Fri$', r'$Sat$', r'$Sun$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel('Day')
plt.ylabel('P(rain)')

for x, y in zip(x, y):
    plt.text(x+0.3, y+0.02, '%.2f' % y)

plt.text(2.35, 1.05, 'Probability of Rainfall')
plt.show()



# Bar graph - Adding text
x = np.arange(7)
y1 = np.random.uniform(size=7)
y2 = np.random.uniform(size=7)
plt.figure(figsize=(6, 5))
plt.title('Weekly Probability of Rainfall')
plt.bar(x+0.1, y1, width=0.4, facecolor='blue', edgecolor='white', alpha=0.6, label='City 1')
plt.bar(x+0.5, y2, width=0.4, facecolor='green', edgecolor='white', alpha=0.6, label='City 2')
plt.ylim(0, 1.15)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5], [r'$Mon$', r'$Tue$', r'$Wed$', r'$Thurs$', r'$Fri$', r'$Sat$', r'$Sun$'])
plt.yticks([0, 0.25, 0.5, 0.75, 1], [r'$0$', r'$0.25$', r'$0.5$', r'$0.75$', r'$1$'])
plt.xlabel('Day')
plt.ylabel('P(rain)')
plt.legend(loc='upper right', frameon=False)
plt.show()



# Histogram
mean = 50
variance = 1
x = mean + variance * np.random.randn(10000)
n, bins, patches = plt.hist(x, bins=50, normed=1, facecolor='blue', alpha=0.3)

import matplotlib.mlab as mlab
envelope = mlab.normpdf(bins, mean, variance)
plt.plot(bins, envelope, 'k-')

plt.xlabel('Score')
plt.ylabel('Probability')
plt.title('Math test scores')
plt.axis([46, 54, 0, 0.5])
plt.grid()
plt.show()


