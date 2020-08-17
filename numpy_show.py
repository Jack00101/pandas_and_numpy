import numpy as np
import time

#创建0-999999的numpy.ndarray
my_arr = np.arange(1000000)
my_list = list(range(1000000))

time1=time.time()

for _ in range(10): my_arr2 = my_arr * 2

time2=time.time()
print("所用时间：%f"%(time2-time1))#所用时间：0.021970

time3=time.time()

for _ in range(10): my_list2 = [x * 2 for x in my_list]

time4=time.time()
print("所用时间：%f"%(time4-time2))#所用时间：0.853718
#创建随机数列
data=np.random.randn(3,2)
print("data:\n",data)
print("data+1:\n",data+1)
print("data行数列数：",data.shape)
print("data维度：",data.ndim)
data=data.reshape(2,3)

list=[[1,2.1,3,4,5,6.3,7,8],[8,7,6,5,4,3,2,1]]
#list->np.array
arr1=np.array(data,dtype=np.int32)
# print(arr1)
print(arr1.dtype)
print("创建np.arrary：")
print(np.zeros(10))
print(np.zeros([3,6]))
#empty中的空并不一定是0，很多数情况下返回的都是为初始化的垃圾值。
print(np.empty([2,3,2]))
print(np.ones([4,6]))
print(np.ones_like(arr1))
#创建对角线为1的对角矩阵
print(np.eye(10))
print(np.identity(10))
#切片
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[:,:,0])
print(arr3d)
#转置
print("转置:")
print(arr3d.T)
# 计算内积
print(np.dot(arr3d.T,arr3d))
my_arr=np.array(my_arr)