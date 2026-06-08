#pandas - for handling structured data - data analyzing and manipulation
#dataframe
#series
#reading csv file
#checking data - pd.head(),.shape,.info(),.describe().....

#dataframe and series
'''
import pandas as pd
data = {'name':['siva','ram','kishore','bayya'],'age':[20,23,25,27]}
df = pd.DataFrame(data)
print(df)
data2 = [10,2,5,6]
ds = pd.Series(data2)
#print(ds)
#print(df['name'])
#print(df['age'])
print(df.iloc[2])  #works everywhere by position, no need index name
print(df.loc[1])  #loc is used when manual indexes are give
df2 = pd.DataFrame(data,index=['r1','r2','r3','r4'])
#print(df2.loc[0]) #not works when manual index are given
print(df2.iloc[2]) #works even manual indexs are given
#reading csv files
'''
#reading csv files
'''
import csv
import pandas as pd
pd.DataFrame([['sridar',25,'avr']],columns=['name','age','city']).to_csv('people.csv',mode='a',index=False,header=False)
a = pd.read_csv('people.csv',nrows =10) #removes header names and displays only 3 rows
print(a)
print(a.head())
a.to_csv("new.csv",index = False,header= False)
print(a[['name','age']])
print(a[a['age']>20])
print(a[(a['age']>21)&(a['name']=='sridar')])
'''
#handling missing data - drop and fill
#NaN = not a number = means missing or empty
'''
import pandas as pd
a = pd.read_csv('people.csv')
print(a)
print(a.isnull()) #checks any missing data in csv files
print(a.isnull().sum()) # no of missing files
print(a.count())
a_cleaned = a.dropna() #drops missing values
print(a_cleaned)
#a_fill = a.fillna(23)
#print(a_fill)
a.columns=['name','age','city']

a['age'] = a['age'].fillna(a['age'].mean())
print(a) 
a.to_csv('people.csv',index=False,header=False)

'''
#creating a best example for all operations
'''
import pandas as pd
import numpy as np
data = {'rollno':[1,16,18,51,32,35,45,9,2,6],
        'name':['a','b','c','d','e','f','g','h','i','j'],
        'age':[17,17,18,19,'',20,21,26,'',24],
        'branch':['cse','cse','csm','ece','cse','ece','csm','ece','csm','csm'],
        'percentage':[90,88,'',75,64,78,77,'',54,66]}
df = pd.DataFrame(data)
df.replace('',pd.NA,inplace=True)
df.to_csv('new.csv',index = False)
print(df)
df_cleaned = df.dropna()
print(df_cleaned)
#adding missed data with mean
'''
'''
df['age'] = df['age'].fillna(df['age'].mean())
df['percentage'] = df['percentage'].fillna(df['percentage'].mean())
print(df)
'''
'''
#now adding missed data with forward and backward fill
#df.fillna(method='ffill',inplace=True) #forward fill for all items in data
#df['age'].fillna(method='ffill',inplace=True)
#df['percentage'].fillna(method='bfill',inplace =True)
print(df)
print(df.dropna(how='all')) #drops if only the entire row is empty or na
print(df.dropna(subset='age')) #drop rows when only age is na
print(df.dropna(axis=1)) #removes all columns with nan

#filtering
print(df[(df['percentage']>75)&(df['percentage']<92)])
print(df[df['percentage']>80])
print(df[df['percentage'].isin(range(54,75))])
#sorting
print(df.sort_values(by='percentage',ascending=False))
print(df.sort_values(by=['percentage','name'])) #if marks equal then sorted by name
'''
#merging and joining - same like sql
#inner join
'''
import pandas as pd
marks=pd.DataFrame({'name':['a','b','c'],
                      'marks':[79,80,65]})
ranks = pd.DataFrame({'name':['a','b','d'],
                      'rank':[2,1,3]})
merge = pd.merge(marks,ranks,on='name')
print(merge.sort_values(by='rank',ascending=True))
#left join
left_merge = pd.merge(marks,ranks,on='name',how='left')
print(left_merge)
#right join 
right_merge = pd.merge(marks,ranks,on='name',how='right')
print(right_merge)
#outer join
outer = pd.merge(marks,ranks,on='name',how='outer')
print(outer)
'''
#concatenation - same as merge with extra future - add columnwise
'''
import pandas as pd 
name = pd.DataFrame({'name':['a','b','c']})
age = pd.DataFrame({'age':[20,21,24]})
conct = pd.concat([name,age],axis=1)
print(conct)
'''
#groupby - groupby column values and perform operation on the values
import pandas as pd
data = {'name':['ram','krishna','ram','krishna'],
        'marks':[91,81,93,83],
        'subject':['math','math','java','java']}
df = pd.DataFrame(data)
group_marks=df.groupby(['name','subject'])['marks'].sum()
print(group_marks)
print(df.describe())
print(df['subject'].value_counts()) #counts subjects
print(df['subject'].unique()) #displays only unique
print(df['marks'].describe()) #describe is used to find outliers - means finding error and that are too impossible values




