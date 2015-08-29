##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  There are three types of edits that can be performed on strings:  insert a
##  character, remove a character, or replace a character.  Given two strings, write a function
##  to check if they are one edit (or zero edits) away

def iq_0105(strA, strB):

    edits = 0
    edits += abs(len(strA)-len(strB))

    skip = False
    if edits == 1:
        skip = True
    if edits >=2:
        return False

    letterCount = {}
    for letter in strA:
        letterCount[letter] = letterCount.get(letter, 0) + 1
    for letter in strB:
        letterCount[letter] = letterCount.get(letter, 0) + 1

    numLetterDiff = 0
    for key in letterCount.keys():
        if(letterCount[key]%2 == 1):
            if(skip):
                skip = False
                continue
            else:
                numLetterDiff +=1
    edits += (numLetterDiff/2)

    if edits >= 2:
        return False
    return True

print(iq_0105("pale", 'ple'))
print(iq_0105("pales", 'pale'))
print(iq_0105("pale", 'bale'))
print(iq_0105("pale", 'bake'))

print(iq_0105("nachos", 'nacho'))
print(iq_0105("nachos", 'nahos'))
print(iq_0105("nachos", 'nbcho'))
