#numpy - numpy is a powerful tool for numerical computations using array for faster data loadingthan pandas
#simply - numpy is like matrices for math and pandas is like sql -table data , clear and structured data
#arrays in python - importing array module or using numpy for arrays
#array module
'''
import array
from array import array  #if we didn't import from array we can use array.array at assigning
nums = array("i",[1,2,3])
print(nums[1])
nums.append(4)     #adding
nums.extend([5,6,7,8,8,9])    #adding multiple items
nums.insert(2,99)        #replacing using index
nums.pop() #removes last
nums.remove(1)
i = nums.index(2)  #searching index
print(i) 
a = nums.count(8)
print(a)
for item in nums:
    print(item)
#converting to list
con = nums.tolist()
print(con)
'''
#numpy
'''
import numpy as np
a = np.array([1,2,3]) #1d array
print(a)
b = np.array([[1,2,3],[4,5,6]])  #2d array with 2rows and 3 columns
c= np.array([[1],[2],[3]])  #2d array with 3rows and 1column
print(b)
print(c)
zeros = np.zeros((2,3))
ones = np.ones((2,2))    #create 1s with 2 rows and 2 columns
r = np.arange(0,10,2)    #creates 1d array with a step of 2
line = np.linspace(0,2,8) #creates in between 8 values by equally dividing
print(zeros)
print(ones)
print(r)
print(line)
'''
'''
#arithmetic operarions
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b,a-b,a*b,a/b)
#scalar operations
print(a*10)
#array statistics
c = np.array([[1,2,3],[4,5,6]])
print(np.sum(c))
print(np.max(c))
print(np.min(c))
print(np.mean(c))
print(np.std(c)) #standard deviation
print(np.median(c))
#array reshaping - transforming structure
print(c.flatten())   #2d - 1d
print(c.reshape((2,3)))  #1d - 2d
print(c.T) #transpose a matrix
'''
#broadcasting - broadcasting some value to arrays without using loops
'''
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b= np.array([10])
print(a+b)  #broadcasting b to a
c = np.array([[1,1,1],[2,2,2]])
print(a+c)
'''
