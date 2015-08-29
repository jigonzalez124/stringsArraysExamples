##  Author:  Jesus Ivan Gonzalez
##  Date:  August 29th 2015

##  Description:  Write an algorithm such that if an element in a matrix MxN is 0, the entire
##  row and column are set to zero

def iq_0108(matrix):

    locZeros = []
    for a in range(len(matrix[0])):
        for b in range(len(matrix)):
            if matrix[b][a] == 0:
                locZeros.append((b,a))

    for pair in locZeros:
        row = pair[0]
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
        col = pair[1]
        for i in range(len(matrix)):
            matrix[i][col] = 0
    print(matrix)

origA = [[1,1,1], [1,5,6], [8,7,6], [1,1,2], [8,0,3]]
iq_0108(origA)
