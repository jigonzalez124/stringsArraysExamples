##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Implement a method to perform basic string compression using the counts of
##  repeated characters.  For example, the string aabcccccaa would become a2b1c5a3.  If the
##  "compressed" string would not become smaller than the original string, your method should
##  return the original string.  


def iq_0106(strA):

    origStrA = strA[:]
    if len(strA) == 1:
        return "%s%d" %(strA,1)
    else:
        listA = list(strA)
        result = []
        breakAllWhiles = False
        while True:
            letter = listA.pop()
            count = 1
            if listA == []:
                temp = [str(count),letter]
                result.extend(temp)
                break
            while(letter == listA[-1]):
                count += 1
                del listA[-1]
                if listA == []:
                    temp = [str(count),letter]
                    result.extend(temp)
                    breakAllWhiles = True
                    break
            if breakAllWhiles:
                break
            else:
                temp = [str(count),letter]
                result.extend(temp)
        if(len(origStrA) <= len(result)):
            print(origStrA)
        else:
            result.reverse()
            print(''.join(result))
        
iq_0106('aabcccccaaa')
iq_0106('Grrrreeeeaaat!!')
iq_0106('Baker')
