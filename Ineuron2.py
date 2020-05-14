# -*- coding: utf-8 -*-
"""
Created on Tue May 12 20:18:30 2020

@author: 714404
"""
#my reduce
def myreduce(fun, seq):
    a=seq[0]
    for i in seq[1:]:
        a=fun(a,i)
        return a
    #----------------------------------------------------------
#my filter    
def myfilter(fun,iterable):
    a=[]
    for i in iterable:
        if fun(i):
            a.append(i)
        return a
  #-------------------------------------------------------------  
word = "ACADGILD"
a=[]
for i in word:
    a.append(i)
print(a)    
#--------------------------------------------------------------
a=[]
l = ['x','y','z']
for i in l:
    for j in range(1,5):
        a.append(i*j)
print(a)
#----------------------------------------------------------------

a=[]
l = ['x','y','z']
for i in range(1,5):
    for j in l:
        a.append(i*j)
print(a)

#----------------------------------------------------------------
a=[]
l=[1,2,3]
for i in range(1,4):
    for j in l:
        a.append([i+j])
print(a)
#---------------------------------------------------------------
a=[]
l=[1,2,3,4]
for i in range(1,5):
    a.append([i+j for j in l])
print(a)
#--------------------------------------------------------------
a=[]
l=[1,2,3]
for i in l:
    for j in l:
        a.append((i,j)) 
print(a)
#---------------------------------------------------------------        
#3.
def longestword(l):
    a=[]
    for i in l:
        a.append(len(i))
        a.sort()
    maxlen=a[-1]
    for j in l:
        if len(j)==maxlen:
            print(j)
            break
    return 
longestword(['My','name', 'is','Saurav','Gaurav'])

#-------------------------------
class area:
    def sides(a,b,c):
        s=(a+b+c)/2 
        return(s*((s-a)*(s-b)*(s-c)))** 0.5

area.sides(3,4,6)        


#----------------------------------    --------------------
def filter_long_word(string,number):
    listwords = []
    for i in range(len(string)):
        if len(string[i]) > number:
          listwords.append(string[i])
    return listwords        
        

filter_long_word(['My', 'Saurav', 'is'], 4)   
    
#-----------------------------------------------------------
def lengthoftword(l):
    a=[]
    for i in l:
        a.append(len(i))
print(a)          

#----------------------------------------------------------
def vowel(l):
    if (l =='a' or 'e' or 'i' or 'o' or 'u'):
        return True

vowel(a)

        