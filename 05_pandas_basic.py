from pandas import Series,DataFrame
import pandas as pd
import numpy as np

'''
obj = Series([4.5,7.2,-5.3,3.6], index=['d','b','a','c'])
print(obj)
obj2 = obj.reindex(['a','b','c','d','e'])
print(obj2)
print(obj.reindex(['a','b','c','d','e'], fill_value=0))
obj3 = Series(['blue','purple','yellow'], index=[0,2,4])
print(obj3)
print(obj3.reindex(range(6),method='ffill'))
print(obj3.reindex(range(6),method='bfill'))

# frame2 = DataFrame(np.arange(9).reshape((3,3)), columns=['Ohio','Texas','California'])
# print(frame2)

frame = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'], columns=['Ohio','Texas','California'])
print(frame)
# print(frame.reindex(['a','b','c','d'],fill_value=10.0))
print(frame.reindex(['a','b','c','d']))
states = ['Texas','Utah','California']
# print(frame.reindex(columns=states, fill_value=100))
print(frame.reindex(columns=states))
# print(frame.reindex(index=['a','b','c','d'], method='ffill', columns=states)) 오류 발생...??
print(frame.reindex(index=['a','b','c','d'], columns=states, fill_value=100))
print(frame)
# print(frame.ix[['a','b','c','d'], states]) 오류 발생...??
print(frame.ix[['a','c','d'], ['Ohio','Texas','California']])
'''

## 5.2.2
'''
obj = Series(np.arange(5.),index=['a','b','c','d','e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d','c']))
print(obj)

data = DataFrame(np.arange(16).reshape((4,4)), index=['Ohio','Colorado','Utah','New York'],
                 columns=['one','two','three','four'])
print(data)
print(data.drop('two',axis=1))
print(data.drop(['Ohio','Colorado']))
# print(data.drop('two'))

obj = Series(np.arange(4.), index=['a','b','c','d'])
print(str(obj[1])+" "+str(obj['b']))
print(obj[2:4])
print(obj[['b','d','a']])
print(obj[[3,1]])
print(obj[obj > 2])
print(obj['b':'d'])
obj['b':'d'] = 5
print(obj)

data = DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],
                 columns=['one','two','three','four'])
print(data)
print(data['two'])
print(data[['three','two']])
print(data[2:4])
print(data[data['three'] > 5])
print(data[2:3])
print(data < 5)
# data[data < 5] = 1000
# print(data)
# print(data.ix['Colorado',['two','three']]) # Deprecated 됐다네... 쩝

print(data.loc[['Colorado','Ohio'], ['two']]) # loc은 label 방식으로 DataFrame 원소를 접근
print(data.loc[data.three > 5, ['three', 'four']])
print(data.loc[:'Utah', ['two','four']])

print(data.iloc[1:3,1:3]) # iloc은 숫자로 DataFrame 원소를 접근
print(data.iloc[:3,[3,0,1]]) # iloc은 숫자로 DataFrame 원소를 접근
print(data.iloc[2,2])
'''


### 5.2.4
'''
S1 = Series([7.3, -2.5, 3.4, 1.5], index=['a','c','d','e'])
S2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a','c','e','f','g'])
print(S1+S2)

df1 = DataFrame(np.arange(9.).reshape((3,3)), columns=list('bcd'), index=['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
print(df2)
print(df1+df2)

df1 = DataFrame(np.arange(12.).reshape((3,4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4,5)), columns=list('abcde'))
# print(df1)
# print(df1+df2)
print(df1.add(df2,fill_value=0))
# print(df2.add(df1,fill_value=0)) 위와 같은 결과
# print(df1.reindex(columns=df2.columns,fill_value=0))


arr = np.arange(12.).reshape((3,4))
print(arr)
print(arr[0])
print(arr-arr[0])

frame = DataFrame(np.arange(12).reshape((4,3)),columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
# series = frame.ix[0] Deprecated 됐으니 아래 것을 쓰자.
series = frame.iloc[0,]
print(frame)
print(series)
print(frame - series)

series2 = Series(range(3), index=['b','e','f'])
print(frame+series2)
series3 = frame['d']
print(series3)
print(frame.sub(series3,axis=0))
print(frame.add(series3,axis=0))
'''

### 5.2.5
'''
frame = DataFrame(np.random.randn(4,3), columns=list('bde'), index=['Utah','Ohio','Texas','Oregon'])
# print(frame)
# print(np.abs(frame))
f = lambda x: x.max() - x.min()
print(frame.apply(f))           # 컬럼에 대해서 실행하는 경우
print(frame.apply(f,axis=1))    # 행에 대해서 실행하는 경우

def f2(x):
    return Series([x.min(),x.max()], index=['min','max'])

print(frame.apply(f2))

format = lambda x: '%.2f' % x
print(frame.applymap(format))
print(frame['e'].map(format))
'''

### 5.2.6
'''
obj = Series(range(4), index=['d','a','b','c'])
print(obj)
print(obj.sort_index())
frame = DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
print(frame.sort_index())
print(frame.sort_index(axis=1,ascending=False))

obj = Series([4,7,-3,2])
print(obj.sort_values())
obj2 = Series([4,np.nan,7,np.nan,-3,2])
print(obj2.sort_values())

frame = DataFrame({'b':[4,7,3,-2], 'a':[0,1,0,1]})
print(frame)
print(frame.sort_values(by='b'))
print(frame.sort_values(by=['a','b'], ascending=False))

obj = Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
print(obj.rank(ascending=False, method='max'))
'''

### 5.2.7
'''
obj = Series(range(5), index = list('aabbc'))
print(obj)
print(obj.is_unique)        # 값이 unique한 것인지 확인
print(obj.index.is_unique)  # 인덱스 값이 unique한 것인지 확인
print(obj['a'])
print(obj['c'])
df = DataFrame(np.random.randn(4,3),index=list('aabb'))
print(df.loc['a'])
print(df.iloc[0:1,0:2])
'''

### 5.3

df = DataFrame([[1.4,np.nan], [7.1,-4.5], [np.nan,np.nan],[0.75,-1.3]],index=list('abcd'),columns=['one','two'])
print(df)
print(df.sum())
print(df.sum(axis=1))
print(df.sum(axis=1, skipna=False))
print(df.idxmax())              # 행 기준으로 최대값이 있는 행의 인덱스를 제시
print(df.idxmax(axis=1))        # 열 기준으로 최대값이 있는 열의 인덱스를 제시

print(df.cumsum())
print(df.cumsum(axis=1))

print(df.describe())

obj = Series(list('ab')*4)
print(obj.describe())

