#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    tryit=N-1
    gettotal=1374393.14
    while tryit != 0: 
        current_city = tryit
        temp=current_city
        unvisited_cities = set(range(0, N))
        unvisited_cities.remove(current_city)
        solution = [current_city]

        def distance_from_current_city(to):
            return dist[current_city][to]
        total=0
        while unvisited_cities:
            next_city = min(unvisited_cities, key=distance_from_current_city)

            unvisited_cities.remove(next_city)
            solution.append(next_city)
            total=total+distance(cities[current_city], cities[next_city])
            current_city = next_city
        total=total+distance(cities[temp], cities[next_city])
        if gettotal>total:
            gettotal=total
        tryit = tryit -1
    print gettotal
        
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
   # print_solution(solution)
