
# coding: utf-8

# In[8]:


# Leitura do arquivo vindo do squad 2

import pandas as pd
import requests

def leitura():
    csv = requests.get("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv").content
    f = open('data.csv', 'wb')
    f.write(csv)
    f.close()
    df = pd.read_csv('data.csv')
    return df


# In[9]:


df = leitura()


# In[12]:


# Criação do scatter
import matplotlib.pyplot as plt
def scatter():
    plt.scatter(df["sepal.length"] , df["sepal.width"] )
    plt.grid( linewidth= 1, linestyle="--")


# In[13]:


scatter()

