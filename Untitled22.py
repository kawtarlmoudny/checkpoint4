#!/usr/bin/env python
# coding: utf-8

# In[10]:


def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three(20,35,19))
    
    
    

    
    


# In[13]:


calcul =lambda a, b:(a+b, a-b)
calcul(40, 10)


# In[ ]:




