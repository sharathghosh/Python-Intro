# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:26:46 2016

@author: sharath
"""

import numpy as np



# 1-dimensional arrays
a = np.array([0, 1, 3, 7, 8, 9])
print a
print type(a)

# 2-dimensional arrays
b = np.array([[1, 2, 3],
              [5, 6, 7],
              [8, 9, 0]])
print b
print type(b)

# Array shapes
print a.shape
print b.shape

# Array sizes
print a.size
print b.size



# Array of zeros and ones of a certain shape
z1 = np.zeros(5)
print z1

z2 = np.zeros((5, 5))
print z2
# shapes are always specified as a tuple for 2-d arrays

o1 = np.ones(3)
print o1

o2 = np.ones((4, 4))
print o2

o3 = np.zeros_like(a)
print a
print o3

o4 = np.ones_like(b)
print b
print o4



# Identity
I = np.identity(5)

I_ = np.eye(5)
print I_
I_1 = np.eye(5, k=1)
print I_1
I_neg1 = np.eye(5, k=-1)
print I_neg1



# Sums and products
A = np.array([[1, 2, 3],
              [3, 5, 7],
              [1, 0, 1]], dtype=float)

B = np.identity(3)
C = A + B
print A
print B
print C

D = A * B # element wise products, not matrix multiplication
print D

D_ = A.dot(B) # this is matrix multiplication
print D_

A_transpose = A.T # transpose A
print A
print A_transpose



x = np.array([1, 2, -3, -3, 8, -2, -1, 4, 5])

# sum of elements of an array
x_sum = np.sum(x)
print x_sum

# product of elements of an array
x_prod = np.prod(x)
print x_prod

# minimum value
x_min = np.min(x)
print x_min

# maximum value
x_max = np.max(x)
print x_max

# mean
x_mean = np.mean(x)
print x_mean

# median
x_median = np.median(x)
print x_median

# index of minumum value
x_argmin = np.argmin(x)
print x_argmin, x[x_argmin]

# index of maximum value
x_argmax = np.argmax(x)
print x_argmax, x[x_argmax]



y = np.array([[4, 5, 2],
              [1, 6, 9]])

# sum of elements of an array
y_sum = np.sum(y)
print y_sum
y_sum_0 = np.sum(y, axis=0)
print y_sum_0
y_sum_1 = np.sum(y, axis=1)
print y_sum_1


# product of elements of an array
y_prod = np.prod(y)
print y_prod
y_prod_0 = np.prod(y, axis=0)
print y_prod_0
y_prod_1 = np.prod(y, axis=1)
print y_prod_1

# minimum value
y_min = np.min(y)
print y_min
y_min_0 = np.min(y, axis=0)
print y_min_0
y_min_1 = np.min(y, axis=1)
print y_min_1

# maximum value
y_max = np.max(y)
print y_max
y_max_0 = np.max(y, axis=0)
print y_max_0
y_max_1 = np.max(y, axis=1)
print y_max_1

# mean
y_mean = np.mean(y)
print y_mean
y_mean_0 = np.mean(y, axis=0)
print y_mean_0
y_mean_1 = np.mean(y, axis=1)
print y_mean_1

# index of minumum value
y_argmin = np.argmin(y)
print y_argmin
y_argmin_0 = np.argmin(y, axis=0)
print y_argmin_0
y_argmin_1 = np.argmin(y, axis=1)
print y_argmin_1

# index of maximum value
y_argmax = np.argmax(y)
print y_argmax
y_argmax_0 = np.argmax(y, axis=0)
print y_argmax_0
y_argmax_1 = np.argmax(y, axis=1)
print y_argmax_1



# Broadcasting
k = np.array([[4, 5, 2],
              [1, 6, 9]])
z = np.array([1, 2, 3])

(r, c) = y.shape # extract row and column from shape information
for row in range(0, r):
    k[row, :] = k[row, :] + z
print k

k = np.array([[4, 5, 2],
              [1, 6, 9]])
z = np.array([1, 2, 3])
k = k + z
print k



k = np.array([[4, 5, 2],
              [1, 6, 9]])

# simple extraction of elements based on a condition
k_less_than_5 = k[k < 5]

z = k < 5
z = z.astype(np.int)
k = k * z

k = np.array([[4, 5, 2],
              [1, 6, 9]])

k[np.logical_and(k < 5, k > 1)]
z = np.logical_and(k < 5, k > 1).astype(np.int)
k = k * z



# Slicing
p = np.array([[4, 5, 2],
              [1, 6, 9],
              [8, 8, 4],
              [3, 1, 0]])
print p

# select a range of rows, all columns
p1 = p[1:3, :]
print p1
p2 = p[1:, :]
print p2

# select all rows, range of columns
p4 = p[:, 1:2]
print p4
p5 = p[:, 1:]
print p5



# Random numbers
r_u = np.random.uniform(size=10)
r_g = np.random.normal(size=25)

r_ua = r_u.reshape((5, 2))
print r_ua

r_ug = r_g.reshape((5, 5))
print r_ug

np.random.seed(0) # set seed before calling RNG to have repeatable results
np.random.uniform()



# Linear, Logarithmic spaced intervals
linear_interval = np.linspace(0, 99, num=5)
log_interval = np.logspace(1, 3, 3)




try:
    print(1/0)
except:
    print "Exception"
finally:
    print "All done!"

aa = [[1, 2], [3, 4]]

new_list = []
for i in aa:
    for j in i:
        new_list.append(j)

new_list = [elem for row in aa for elem in row]
