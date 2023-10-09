#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns # For Data Visualization
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as nm


# In[2]:


get_ipython().system('pip install colorama')
from colorama import Fore, Back, Style


# In[3]:


get_ipython().system('pip install wordcloud')


# In[4]:


from wordcloud import WordCloud
from wordcloud import STOPWORDS


# In[5]:


test=pd.read_csv("testhr.csv")
train=pd.read_csv("trainhr.csv")


# In[6]:


pd.set_option("display.max_rows",10)
pd.set_option("display.max_column",15)
pd.set_option("display.max_colwidth",10)
pd.set_option("display.width",2000)
test.head()


# In[7]:


train.head()


# In[8]:


test["department"]


# In[9]:


train["department"]


# # •	Getting info of train

# In[10]:


#GETTING INFO OF TRAIN

train.info()


# # •	checking if there is any NULL value in the dataset

# In[11]:


#•	checking if there is any NULL value in the dataset in train
train.isnull().any()


# In[12]:


#getting sum of null quantities
train.isnull().sum()


# # ========= •	looking at the most popular departments   ============#

# In[13]:


#THIS IS FOR THE TRAIN CASE
df1 = train.pivot_table(index = ['department'], aggfunc ='size')
print(df1)


# In[14]:


#THE BELOW IS THE SORTED FOR THE MOST POPULAR DEPARTMENTS IN TRAIN CASE


# In[15]:


sort_dep1=df1.sort_values(ascending=False)
sort_dep1


# #1)THE BELOW IS THE SORTED BAR GRAPH FOR # checking the Most Popular Departments in TRAIN.HR

# In[16]:


bargraph = sort_dep1.plot.bar(x = "department", y = "number of employees", fontsize="10")


# In[17]:


#THE BELOW IS THE SORTED FOR THE MOST POPULAR DEPARTMENTS IN TEST CASE


# In[18]:


df2=test["department"].value_counts()
df2


# In[19]:


stopword=set(STOPWORDS)
#print(stopword)


# In[ ]:


wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS).generate(str(test["department"]))
# Display the generated image
plt.rcParams['figure.figsize']=(13,6)
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Most popular departments for testhr',fontsize=20)
plt.axis("off")
plt.grid()
plt.show()


# # ======== •	checking the no. of Employees Promoted     ========#

# In[ ]:


promote=train["is_promoted"].value_counts()
print("\33[1;49;36m",promote)


# In[ ]:


print(Fore.GREEN +"number of people got promoted are\33[4;36;91m", promote[1])


# # •	finding the %age of people promoted and plot a scatter plot over data

# In[ ]:


per=(promote[1]/promote[0])*100
print(" \33[1;49;93m percentage of people promoted are \33[1;49;36m {:.2f}%".format(per))


# In[ ]:


plt.hist(train["is_promoted"])
plt.title("PLOT TO SHOW the gap between promoted and non-pormoted people",fontsize=20)
plt.xlabel("0 - no promotion     1 - promotion ",fontsize=20)
plt.grid()
plt.show()


# ==============================#PLOTTING A SCATTER PLOT =================================

# In[ ]:


x=train["avg_training_score"] 
y=train["is_promoted"]
z=[]
for i in range(len(y)):
    if y[i]==1:
        z.append(x[i])
print("the below is the average score of the people who were promoted\n")
count=pd.Series(z).value_counts()
print(count)


# In[ ]:


train.plot(x="avg_training_score",y="is_promoted", kind="scatter")


# # •	checking the distribution of the avg_training score of the Employees==#

# In[ ]:


avg_sc=train["avg_training_score"].value_counts()
print(avg_sc)


# In[ ]:


#this is the average training score of trainhr case
plt.rcParams["figure.figsize"]=(15,7)
sns.histplot(train["avg_training_score"],color="cyan")
plt.title("average training  score by the people")
plt.xlabel("average training score",fontsize=20)
plt.ylabel("count",fontsize=20)
plt.ylim(0, 4500)
plt.show()


# =========================#the below is the distribution of average training score in test hr case=============================

# In[ ]:


avg_sc2=test["avg_training_score"].value_counts(ascending=True)
avg_sc2


# In[ ]:


bargraph3 = avg_sc2.plot.bar(x = "average training score", y = "number of employees got ", fontsize="10")


# # ==== •	Counting the number of persons who have won the award======

# In[ ]:


award=train["awards_won?"].value_counts()
award


# In[ ]:


plt.hist(train["awards_won?"],color=["lightblue"], ec="yellow",lw=2)
plt.title("PLOT TO SHOW the the number of people who won awards ",fontsize=20)
plt.xlabel(f"0 - no awards won   1 - awards won \n\nNUMBER OF PEOPLE WHO WON AWARDS ARE {award[1]}",fontsize=20,)
plt.show()


# In[ ]:


#Plot a donut  chart for visualizing %age of emp who won award
size=train['awards_won?'].value_counts()
colors=['red','green']
exp=[0,.1]
labels=("No awards won","Award won")
circle=plt.Circle((0,0),0.7,color='white')
plt.rcParams['figure.figsize']=(8,8)
plt.pie(size,labels=labels,colors=colors,autopct="%0.2f%%",explode=exp)
plt.title("percentage of employees who won  awards",fontsize=30)
p=plt.gcf()
p.gca().add_artist(circle)
plt.legend()
plt.show()


# # ======•	checking the distribution of length of service=======#

# In[ ]:


service=train["length_of_service"].value_counts()
service


# In[ ]:


sns.histplot(train["length_of_service"],color="green")
plt.title("the plot shows number of poeple and their length of service in years",fontsize=20)
plt.xlabel("length of service in years ",fontsize=20)
plt.ylabel("count",fontsize=20)
plt.show()



# In[ ]:


#using distplot to plot the desity as well

sns.distplot(train["length_of_service"], kde = True, color ='red', bins = 34,hist_kws={"rwidth":0.75,'edgecolor':'black', 'alpha':1.0,})
plt.title("the plot shows number of poeple and their length of service in years",fontsize=20)
plt.xlabel("length of service in years ",fontsize=20)
plt.ylabel("count",fontsize=20)

plt.show()


# # •	checking the distribution of age of Employees in the company =======

# In[ ]:


years=train["age"]
years


# In[ ]:


age=years.value_counts()
age


# In[ ]:


years2=test["age"].value_counts(ascending=True)
years2


# In[ ]:


bargraph4 = age.plot.bar(x = "age of the employee", y = "number of employees having the same  age ", fontsize="10",color="g",width=.5,alpha=0.50)
bargraph5 = years2.plot.bar(x = "age of the employee", y = "number of employees having the same  age  ", fontsize="10",color="r",width=.5,alpha=0.25)
plt.legend()
plt.xlabel('age of the employee')
plt.ylabel('number of employees having the same  age ')
plt.title("distribution of age of Employees in the company",fontsize=20)
# Print the  bar graph
plt.show()


# # •	checking the different no. of training done by the employees========

# In[ ]:




