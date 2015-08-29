##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Given two strings, str1 and str2, write code to check if one string is a
##  rotation of the other substring

def iq_0109(str1, str2):
    if(len(str1)!=len(str2)):
        return False

    for i in range(len(str1)):
        if(str1 == str2):
            return True
        str1 = str1[1:]+str1[0]
    return False

print(iq_0109("waterbottle", "erbotewat"))
print(iq_0109("waterbottle", "erbotewat"))
print(iq_0109("waterbottle", "bottlewater"))
