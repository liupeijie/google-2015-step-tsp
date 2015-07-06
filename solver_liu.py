#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.trunc(math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2))
    #return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities):
    N = len(cities)  
    size=N
    matrixColumn = [[0] * N for i in range(N)]
    matrixRow = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            matrixRow[i][j] = matrixRow[j][i] = distance(cities[i], cities[j]) 
            matrixRow[i][i] = ""
    #print matrixRow
    #solution = [[0] * N for i in range(N)]
    begin=[[0] * N for i in range(N)]
    next=[[0] * N for i in range(N)]
    num=0
    special=0
    km=0
    while size!=0:
        
        for i in range(N):
            # get row minimization
            k = min(matrixRow[i])

            if k != 0 and k != "":
                
                for j in range(N):
                    if j!=i and matrixRow[i][j] != "":
                        # delta to minimization
                        matrixRow[i][j] = matrixRow[i][j] - k;

        for i in range(N):
            for j in range(N):
                matrixColumn[j][i]=matrixRow[i][j]

        for i in range(N):
                # get column minimization
                k=min(matrixColumn[i])
                
                if k != 0 and k!= "":
                    for j in range(N):
                        if j!=i and matrixColumn[i][j] != "":
                            # delta to minimization
                            matrixColumn[i][j] = matrixColumn[i][j] - k
        
        for i in range(N):
            for j in range(N):
                matrixRow[j][i]=matrixColumn[i][j]

        print matrixRow
        # calculate panelty's of all 0's

        Column = [[0] * N for i in range(N)] 
        Row = [[0] * N for i in range(N)]  
        Zero = 0
      
        for i in range(N):
            for j in range(N):
                checkStart=i
                checkTo=j
                
                if matrixRow[i][j]==0 :
                    for k in range(N):
                        if k != j :
                            Row[i][k] = matrixRow[i][k]
                        else:
                            Row[i][k] = ""
                    for s in range(N):
                        if s !=i:
                            Column[j][s] = matrixRow[s][j]
                        else:
                            Column[j][s] = ""              
                    
                 
                        minColunm=min(Column[j])
                        minRow=min(Row[i])
                        if minColunm != "" and minRow != "":
                            countZero=minColunm+minRow
                        else:
                            countZero = 0;

                        if countZero >= Zero:
                            Zero = countZero
                            start = i
                            to = j
        if start == 6 :
            temp = start
            start=to
            to=temp

        begin[num]=start
        next[num]=to
        km=km+distance(cities[start],cities[to])
        num=num+1

        for q in range(N):
            matrixRow[start][q] = ""
            matrixRow[q][to] = ""
            matrixRow[to][start]=""

        size=size-1

    print begin
    print next
    print km
    return begin


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)