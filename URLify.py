##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Write a method to replace all spaces in a string with '%20'.  You may assume
##  that the string has suffcient space at the end to hold the additional characters and that
##  you are given the 'true' length of a string.

def iq_0103(strA):
    strA = strA.split()
    return "%20".join(strA)


print(iq_0103("Mr John Smith        "))
