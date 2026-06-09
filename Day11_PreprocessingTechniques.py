import pandas as pd
import seaborn as sns

#Loading titanic data
df = sns.load_dataset("titanic")
# print(df)

df.to_csv("titanic.csv", index=False)
titanic_data = pd.read_csv("titanic.csv")
# print(titanic_data)

df2 = sns.load_dataset("iris")
# print(df2)

df2.to_csv("iris.csv", index=False)
iris_data = pd.read_csv("iris.csv")

# print(titanic_data.describe())
# print(iris_data.describe())

d1 = pd.DataFrame({"city":["delhi", "DELHI", "Delhi", "deLhi"]})
count = d1["city"].value_counts()
print(count)

d1["city"] = d1["city"].str.lower()
print(d1["city"].value_counts())

print(titanic_data.isnull().sum())
#there are 177 missing values or null values present in the age section in titatnic data.
#similarly , 688 in deck section, 2 in embarked.

# titanic_data["age"] = titanic_data["age"].fill

titanic_data.drop("deck", axis=1, inplace=True)

print(titanic_data)  #only DataFrame in ram is updated , no deck column removed in file

# titanic_data.to_csv("titanic.csv", index=False) #this will update the file 

print(titanic_data.shape)
print(titanic_data.duplicated().value_counts())

cleaned_data = titanic_data.drop_duplicates()
print(cleaned_data.shape)
print(cleaned_data.duplicated().value_counts())


#if you wanted to save 
#cleaned_data.to_csv("titanic.csv",index=False)

# conversion of datatypes

df3 = pd.DataFrame({"age":[23.5,34.6,29]})
print(df3)

print(df3["age"].astype(int))


#Detection of outliers using visualization

df4 = pd.DataFrame({"salary": [2000,2500,3000,4000,5000,60000]})
print(df4)

import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(df4["salary"])
# plt.show()
# plt.savefig("salary.png")   #if , image displaying fails , use this line to directly save and visualize

#using histogram
plt.figure()
plt.hist(df4["salary"],bins=2,edgecolor="black")
# plt.show()

new_titanic_data = titanic_data.dropna()  #this removes entire null or missed values.
print(new_titanic_data)
print(new_titanic_data.isnull().sum())

#plotting scatter graph
plt.figure()
plt.scatter(new_titanic_data["age"],new_titanic_data["fare"])
plt.show()


#while observing the scatter plot , we find that the fare is inequivalent, that shows two values as outlier

print(new_titanic_data[new_titanic_data["fare"] > 450])

new_titanic_data2 = new_titanic_data[new_titanic_data["fare"] < 450] #simply we removed the outliers
print(new_titanic_data2) 

#we can also save this by 
#new_titanic_data2.to_csv("titanic.csv",index = False)

#try to check by using scatter plot
plt.figure()
plt.scatter(new_titanic_data2["age"],new_titanic_data2["fare"])
plt.title("new_titanic_data2")

plt.show()

#Inter Quartile Range technique 

data = {'name':['a','b','c','d'],
        'marks':[99,98,980,89]}
df = pd.DataFrame(data)
print(df)
#we can find outliers by using describe
print(df.describe())   #values are wrong bcz max marks is 100 but mistakenly typen 980
q3 = df['marks'].quantile(0.75)
q1 = df['marks'].quantile(0.25)
iqr = q3 - q1    #interquartile range
lower = q1-1.5*iqr
upper = q3+1.5*iqr
outliers = df[(df['marks']<lower)|(df['marks']>upper)]
print(outliers)

cleaned_df = df[(df['marks']>=lower)&(df['marks']<=upper)]

#but when we want to manage 
mean_marks=df[(df['marks']>=lower) & (df['marks']<=upper)]['marks'].mean()
print(mean_marks)
df['marks'] = df['marks'].apply(lambda x:mean_marks if (x > upper or x < lower) else x)
print(df)