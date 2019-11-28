#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[1]:


import numpy as np
def gradient_descent_algo(x,y):
    m_curr = c_curr = 0;    # Initializing m&c y = mx+c equation c_curr(bias)
    indices = 10             #no. of iterartions
    length = len(x)          #n
    learning_rate = 0.05
    
    for i in range(indices):
        y_predict = m_curr * x + c_curr                #y-prediction formulae
        
        cost_fun = (1/length) * sum([val ** 2 for val  in (y-y_predict)])  ##Cost or mean squared error function
        
        md = -(2/length) * sum(x * (y-y_predict))      #derivation of m
        cd = -(2/length) * sum(y-y_predict)            #derivation c(bias)
        
        m_curr = m_curr - learning_rate * md          
        c_curr = c_curr - learning_rate * cd         #calculating m & c with learning rate
        print("m value is  : {},  b value is : {}, cost function value is : {}, iterations : {},  " .format(m_curr,c_curr,cost_fun,i))
        
x = np.array([1,2,3,4,5])
y = np.array([7,12,13,10,11])

gradient_descent_algo(x,y)
        
    


# In[ ]:




