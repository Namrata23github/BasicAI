#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
def linearRegression(x,y,ifStand):
    x_train,x_test,y_train,y_test=train_test_split(x,y)
    x_train_data =x_train
    x_test_data = x_test
    if (ifStand == True):
        stdScaler = StandardScaler()
        stdScaler.fit(x_train)
        x_train_data = stdScaler.transform(x_train)
        x_test_data = stdScaler.transform(x_test)
    
    seModel = LinearRegression()
    seModel.fit(x_train_data, y_train)
    print( "Train score", seModel.score(x_train_std,y_train))
    print( "Test score", seModel.score(x_test_data,y_test))
    return seModel;


# In[ ]:




