##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Given two strings, write a method to decide if one is permutation of the other



def iq_0102(stringA, stringB):

    #Checks to see if inputs are strings.  if true, return invalid
    if(type(stringA) != str or type(stringB) != str):
        return "Invalid input"

    #check which is smaller/longer string
    if(len(stringA) <= len(stringB)):
        shortStr = stringA
        longStr = stringB
    else:
        shortStr = stringB
        longStr = stringA

    
    for i in range(len(longStr)-len(shortStr)+1):
        if shortStr == longStr[i:i+len(shortStr)]:
            return True
    return False

print(iq_0102("nachos", 'cho'))
print(iq_0102("dog", 'horde'))
print(iq_0102("mouse", 'mos'))
print(iq_0102("mouse", 'ou'))
print(iq_0102("mouse", 1))
