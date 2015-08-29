##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Implement an algorithm to determine if a string has all unique characters.

def iq_0101(string):
    for index in range(len(string)):
        if string[index] in string[:index]+string[index+1:]:
            return True
    return False

print(iq_0101("nachos"))
print(iq_0101("where"))
print(iq_0101("cat"))
print(iq_0101("absolute"))
