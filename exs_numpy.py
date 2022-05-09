#Submitted by Keren Or Hadad 208025205

import numpy as np
#1
x = np.arange(21)
print("my vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1

print(x)

"""
output:
my vector:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
After changing the sign of the numbers in the range from 9 to 15:
[  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17
  18  19  20]
"""

#2

v = np.linspace(10, 49, 5)
print("Length 10 with values evenly distributed between 5 and 50:")
print(v)

"""
output:
Length 10 with values evenly distributed between 5 and 50:
[10.   19.75 29.5  39.25 49.  ]
"""

#3

m= np.arange(10,22).reshape((3, 4))
print("Original matrix:")
print(m)
print("Number of rows and columns of the said matrix:")
print(m.shape)

"""
output:
Original matrix:
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
Number of rows and columns of the said matrix:
(3, 4)
"""
#4

x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)

"""
output:
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
"""

#5
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])
print("Original vector:")
print(v)
print("Original matrix:")
print(m)
result = np.empty_like(m)
for i in range(4):
  result[i, :] = m[i, :] + v
print("\nAfter adding the vector v to each row of the matrix m:")
print(result)

"""
output:
Original vector:
[1 1 0]
Original matrix:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

After adding the vector v to each row of the matrix m:
[[ 2  3  3]
 [ 5  6  6]
 [ 8  9  9]
 [11 12 12]]

"""

#6
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show()
"""
output
Plot the points using matplotlib:
+ the image
"""

#7

nums = np.arange(16, dtype='int').reshape(-1, 4)
print("Original array:")
print(nums)
print("\nNew array after swapping first and last rows of the said array:")
new_nums = nums[::-1]
print(new_nums)

"""
output:
Original array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

New array after swapping first and last rows of the said array:
[[12 13 14 15]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [ 0  1  2  3]]

"""

#8

nums = np.array([[5.54, 3.38, 7.99],
              [3.54, 8.32, 6.99],
              [1.54, 2.39, 9.29]])
print("Original array:")
print(nums)
n = 8.32
r = 18.32
print("\nReplace elements of the said array which are equal to ",n,"with",r)
print(np.where(nums == n, r, nums))
print("\nReplace elements with of the said array which are less than",n,"with",r)
print(np.where(nums < n, r, nums))
print("\nReplace elements with of the said array which are greater than",n,"with",r)
print(np.where(nums > n, r, nums))

"""
output:
Original array:
[[5.54 3.38 7.99]
 [3.54 8.32 6.99]
 [1.54 2.39 9.29]]

Replace elements of the said array which are equal to  8.32 with 18.32
[[ 5.54  3.38  7.99]
 [ 3.54 18.32  6.99]
 [ 1.54  2.39  9.29]]

Replace elements with of the said array which are less than 8.32 with 18.32
[[18.32 18.32 18.32]
 [18.32  8.32 18.32]
 [18.32 18.32  9.29]]

Replace elements with of the said array which are greater than 8.32 with 18.32
[[ 5.54  3.38  7.99]
 [ 3.54  8.32  6.99]
 [ 1.54  2.39 18.32]]

"""

#9

nums1 = np.array([[2, 5, 2],
              [1, 5, 5]])
nums2 = np.array([[5, 3, 4],
              [3, 2, 5]])
print("Array1:")
print(nums1)
print("Array2:")
print(nums2)
print("\nMultiply said arrays of same size element-by-element:")
print(np.multiply(nums1, nums2))

"""
output:
Array1:
[[2 5 2]
 [1 5 5]]
Array2:
[[5 3 4]
 [3 2 5]]

Multiply said arrays of same size element-by-element:
[[10 15  8]
 [ 3 10 25]]

"""
#10
a = np.array([[4, 6],[2, 1]])
print("Original array: ")
print(a)
print("Sort along the first axis: ")
x = np.sort(a, axis=0)
print(x)
print("Sort along the last axis: ")
y = np.sort(x, axis=1)
print(y)

"""
output:
Original array: 
[[4 6]
 [2 1]]
Sort along the first axis: 
[[2 1]
 [4 6]]
Sort along the last axis: 
[[1 2]
 [4 6]]

"""
#11

x = np.eye(3)
print(x)

"""
output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

#12

x = np.zeros((3, 1, 4))
print(np.squeeze(x).shape)

"""
output:
(3, 4)
"""

#13

a = np.array([[10],[20],[30]])
b = np.array([[40],[50],[60]])
c = np.dstack((a, b))
print(c)

"""
output:
[[[10 40]]

 [[20 50]]

 [[30 60]]]
"""

#14

x = np.arange(4)
print("One dimensional array:")
print(x)
y = np.arange(8).reshape(2,4)
print("Two dimensional array:")
print(y)
for a, b in np.nditer([x,y]):
    print("%d:%d" % (a,b),)

"""
output:
One dimensional array:
[0 1 2 3]
Two dimensional array:
[[0 1 2 3]
 [4 5 6 7]]
0:0
1:1
2:2
3:3
0:4
1:5
2:6
3:7
"""

#15
np.random.seed(32)
nums = np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
print(nums)

"""
output:
[[[215  42 224 219  43]
  [166  69  15 133 255]
  [105  95  54  37 201]
  ...
  [240  22  66 232 132]
  [ 13  85  53 220 170]
  [249  62 221 146  69]]

 [[ 73  79 148 132 164]
  [  3  93  98 138 200]
  [174  34  31 208 130]
  ...
  [ 15 252  41  64  39]
  [188 216 223 124  27]
  [ 85 112 240 116 231]]

 [[227  50 243  20 171]
  [ 12  66 108 102  63]
  [107  54   0   0 173]
  ...
  [215  46  57  99 151]
  [243 199  31  28 179]
  [143   7  30 175 190]]

 ...

 [[214  64  64 212  62]
  [140  44 217  17 164]
  [226 146 247  53 199]
  ...
  [189  68  49 117  63]
  [ 14  17 109  82  92]
  [155 221 135 184 231]]

 [[132 194 160 136 102]
  [132 244 230 117 181]
  [146 245  21 164  29]
  ...
  [125 240 243 190 240]
  [137  41 157 117 155]
  [ 20  92  72 182  41]]

 [[120  45 198 218 190]
  [ 42 150 190 103 106]
  [164  71 220 114  59]
  ...
  [143  20 219 154  85]
  [219 190 170 227 246]
  [ 39  14 127 230 158]]]

"""

#16

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
#Sort by studen_id then by student_height
indices = np.lexsort((student_id, student_height))
print("Sorted indices:")
print(indices)
print("Sorted data:")
for n in indices:
  print(student_id[n], student_height[n])


"""
output:
Sorted indices:
[4 0 5 3 6 1 2]
Sorted data:
1682 38.0
1023 40.0
5241 40.0
1671 41.0
4532 42.0
5202 42.0
6230 45.0
"""

#17

x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 =  np.median(x)
print("\nMedian of said array:")
print(r1)

"""
output:
Original array:
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]

Median of said array:
5.5
"""

#18
print("Number of days, February, 2016: ")
print(np.datetime64('2016-03-01') - np.datetime64('2016-02-01'))
print("Number of days, February, 2017: ")
print(np.datetime64('2017-03-01') - np.datetime64('2017-02-01'))
print("Number of days, February, 2018: ")
print(np.datetime64('2018-03-01') - np.datetime64('2018-02-01'))

"""
output:
Number of days, February, 2016: 
29 days
Number of days, February, 2017: 
28 days
Number of days, February, 2018: 
28 days
"""




