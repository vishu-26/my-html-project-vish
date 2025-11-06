#!/usr/bin/env python
# coding: utf-8

# In[17]:


#LIST's

l=eval(input("Enter a List:- "))
l.sort()
small=min(len(l[0]),len(l[-1]))
pre=""
for i in range(small):
    if l[0][i]==l[-1][i]:
        pre+=l[0][i]
    else:
        break
if pre:
    print(pre)
else:
    print(-1)


# In[16]:


#WAP to find numbers from a list which are >10 and has odd 1st & last digit

l=eval(input("Enter a List:- "))
l1=[]
for i in l:
    if i>10:
        st=str(i)
        f_d=st[0:1]
        l_d=st[-1:-2:-1]
        if int(f_d)%2!=0 and int(l_d)%2!=0:
            l1.append(i)
        else:
            continue
print(l1)


# In[20]:


# Rail Fence Cipher

s=input("Enter a Sentence:- ")
k=int(input("Enter no. key to divide in parts:- "))
s1=""

for i in range(k):
    s1=s1+s[i: :k]
print(s1)


# In[24]:


# DICTIONARY

d={}
print(type(d))

d0={1:'Apple',2:'Banana'}# dict[ke:value],key-->immutable(str,int,tuple) so we can't change,value we can change
print(d0)

d1={1:'A',2:'B',3:'C',2:'D'}
print(d1)

L=[('name','abc'),('age',18),('marks',50)]
d2=dict(L)
print(d2)

