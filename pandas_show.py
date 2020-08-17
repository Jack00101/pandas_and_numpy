import pandas as pd
import numpy as np
#通过二位数组创建数据框dataframe
arr1=np.arange(12).reshape(4,3)
print(arr1)
print(type(arr1))
df1=pd.DataFrame(arr1)
print(df1)
print(type(df1))
#通过字典创建
arr2={'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12],'d':[13,14,15,16]}
print(arr2)
print(type(arr2))
df2=pd.DataFrame(arr2)
print(df2)
print(type(df2))
arr3={'one':{'a':1,'b':2,'c':3,'d':4},'two':{'a':5,'b':6,'c':7,'d':8},'three':{'a':9,'b':10,'c':11,'d':12}}
df3=pd.DataFrame(arr3)
print(df3)
#通过dataframe创建dataframe
# df4=df3[['one','three']]
df4=df3[['one','two']]
print(df4)
#series序列
s4=pd.Series(np.array([1,2,3,4,5,6]))
print(s4)
print(s4.index)
s4.index=['a','b','c','d','e','f']
print(s4)

stu_dic = {'Age':[14,13,13,14,14,12,12,15,13,12,11,14,12,15,16,12,15,11,15],
'Height':[69,56.5,65.3,62.8,63.5,57.3,59.8,62.5,62.5,59,51.3,64.3,56.3,66.5,72,64.8,67,57.5,66.5],
'Name':['Alfred','Alice','Barbara','Carol','Henry','James','Jane','Janet','Jeffrey','John','Joyce','Judy','Louise','Marry','Philip','Robert','Ronald','Thomas','Willam'],
'Sex':['M','F','F','F','M','M','F','F','M','M','F','F','F','F','M','M','M','M','M'],
'Weight':[112.5,84,98,102.5,102.5,83,84.5,112.5,84,99.5,50.5,90,77,112,150,128,133,85,112]}
student = pd.DataFrame(stu_dic)
#前五个数据
print(student.head())
#后五个数据
print(student.tail())
#查询指定行
print(student.loc[[0,2,4,5,7]])
#查询指定列
print(student[['Name']])
print(student.loc[:,['Name']])
#统计分析
np.random.seed(1234)
d1 = pd.Series(2*np.random.normal(size = 100)+3)
d2 = np.random.f(2,4,size = 100)
d3 = np.random.randint(1,100,size = 100)

print('非空元素计算: ', d1.count()) #非空元素计算
print('最小值: ', d1.min()) #最小值
print('最大值: ', d1.max()) #最大值
print('最小值的位置: ', d1.idxmin()) #最小值的位置，类似于R中的which.min函数
print('最大值的位置: ', d1.idxmax()) #最大值的位置，类似于R中的which.max函数
print('10%分位数: ', d1.quantile(0.1)) #10%分位数
print('求和: ', d1.sum()) #求和
print('均值: ', d1.mean()) #均值
print('中位数: ', d1.median()) #中位数
print('众数: ', d1.mode()) #众数
print('方差: ', d1.var()) #方差
print('标准差: ', d1.std()) #标准差
print('平均绝对偏差: ', d1.mad()) #平均绝对偏差
print('偏度: ', d1.skew()) #偏度
print('峰度: ', d1.kurt()) #峰度
print('描述性统计指标: ', d1.describe()) #一次性输出多个描述性统计指标
def stats(x):
	return pd.Series([x.count(),x.min(),x.idxmin(),x.quantile(.25),x.median(),x.quantile(.75),
                      x.mean(),x.max(),x.idxmax(),x.mad(),x.var(),x.std(),x.skew(),x.kurt()],
                     index = ['Count','Min','Whicn_Min','Q1','Median','Q3','Mean','Max',
                              'Which_Max','Mad','Var','Std','Skew','Kurt'])
print(stats(d1))
df = pd.DataFrame(np.array([d1,d2,d3]).T,columns=['x1','x2','x3'])
print(df.head())
print(df.apply(stats))
#统计离散变量的观测数、唯一值个数、众数水平及个数
print(student['Sex'].describe())
#相关系数（corr）和协方差矩阵（cov）
#关于相关系数的计算可以调用pearson方法或kendell方法或spearman方法，默认使用pearson方法
print(df.corr())
print(df.corr('spearman'))