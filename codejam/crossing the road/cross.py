from __future__ import division
from math import ceil
from heapq import heappush, heappop

MAX = 303030303030303
BLOCK_TIME = 2
INTERSECTION_TIME = 1

class ShortestPath:
    def __init__(self, n, m, t):
        self.n = n
        self.m = m
        self.time = t

def solve(grid):
    modifiers = [(-1,0), (0,1), (1,0), (0,-1)]
    sp = [[MAX for i in range(len(grid[0])*2)] for j in range(len(grid)*2)]
    sp[len(sp)-1][0] = 0
    
    heap = []
    heappush(heap, ShortestPath(len(sp) - 1, 0, 0))
    
    while len(heap) > 0:
        top = heappop(heap)
        # shorter distance already found
        if sp[top.n][top.m] > top.time:
            continue

        for i,v in enumerate(modifiers):
            (n, m) = (top.n + v[0], top.m + v[1])
            if 0 <= n < len(sp) and 0 <= m < len(sp[0]):
                t = top.time + time_to_cross(grid, top, n, m, i)
                if (t < sp[n][m]):
                    sp[n][m] = t
                    heappush(heap, ShortestPath(n, m, t))
                
    return sp[0][len(sp[0]) -1]

def time_to_cross(grid, sp, n, m, direction):
    if block(sp, n, m):
        return BLOCK_TIME
    else:
        is_ns = direction % 2 == 0
        (S, W, T) = grid [sp.n // 2][sp.m // 2]
        ct = S + W
        elapsed = (sp.time % ct - T % ct) % ct
        ns_green = elapsed < S
        
        if is_ns and ns_green or not is_ns and not ns_green:
            return INTERSECTION_TIME
        elif is_ns and not ns_green:
            return ct - elapsed + INTERSECTION_TIME
        else:
            return S - elapsed + INTERSECTION_TIME
    
def block(sp, n, m):
    return ceil(sp.n/2) == ceil(n/2) and ceil(sp.m/2) == ceil(m/2)

def process(file):
    N, M = read_int_row(file)
    grid = []
    for i in range(N):
        t0 = read_int_row(file)
        t1 = []
        for j in range(0,  M*3, 3):
            t1.append((t0[j], t0[j+1], t0[j+2]))
        grid.append(t1)
    return solve(grid)

def read_int_row(file):
    return [int(x) for x in  file.readline().split(' ')]

if __name__ == "__main__":
    file = open ("B-small-practice.in", "r")
    maps = int(file.readline()) + 1
    cases = []
    for i in range(1,maps):
        print "Case #%d: %d" %(i, process(file))
