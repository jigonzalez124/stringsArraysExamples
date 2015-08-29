##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Given a string, write a function to check if it is a permutation of a palindrome.
##  A palindrome is a word or phrase that is the same forwards and backwards.  A permutation is a
##  rearrangement of letters.  The palindrome does not need to be limited to just dictionary words

def iq_0104(strA):
    strA = strA.replace(" ", "")
    strA = strA.lower()
    lenA = len(strA)

    letterCount = {}
    for letter in strA:
        letterCount[letter] = letterCount.get(letter, 0) + 1

    pivotExist = 0
    for key in letterCount.keys():
        if(letterCount[key]%2 == 0):
            continue
        elif(letterCount[key]%2 == 1):
            if pivotExist == 0:
                pivotExist = 1
            else:
                return False
    return True
    
                    
print(iq_0104("Tact Coam"))
print(iq_0104("Tact Coa"))
print(iq_0104("Nac|hos |  hoNacs"))
print(iq_0104("Nach||os b a soNach"))
