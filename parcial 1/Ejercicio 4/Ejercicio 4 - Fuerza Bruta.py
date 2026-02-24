# Stones on the Table - Brute Force Approach
# Codeforces Problem 266A
# This solution uses a brute force strategy by repeatedly removing stones
# until no two adjacent stones have the same color.

def min_stones_to_remove_bruteforce(s):
    removals = 0
    stones = list(s)
    
    i = 0
    while i < len(stones) - 1:
        if stones[i] == stones[i + 1]:
            stones.pop(i + 1)
            removals += 1
        else:
            i += 1
            
    return removals


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    
    print(min_stones_to_remove_bruteforce(s))
