#import sys
from functools import lru_cache
#sys.setrecursionlimit(5000)

def rules(num: int):
    #Change to 1
    if num == 0:
        return [1]

    #Splitting even len
    s = str(num)
    n = len(s)
    if n % 2 == 0:
        left = int(s[:n//2])
        right = int(s[n//2:])
        return [left, right]

    #Multiply bu 2024
    return [num * 2024]

@lru_cache(maxsize=None)
def count_pebbles(num: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    new_pebbles = rules(num)
    return sum(count_pebbles(n, blinks - 1) for n in new_pebbles)

def total_pebbles(pebbles, blinks):
    return sum(count_pebbles(num, blinks) for num in pebbles)

pebbles = [0, 7, 198844, 5687836, 58, 2478, 25475, 894]
blinks = 75

print(total_pebbles(pebbles, blinks))