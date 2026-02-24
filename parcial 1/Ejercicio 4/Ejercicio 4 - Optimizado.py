# Stones on the Table
# Codeforces Problem 266A
# Calculates the minimum number of stones to remove so that no two adjacent stones have the same color

def min_stones_to_remove(n, s):
    removals = 0
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            removals += 1
            
    return removals


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    
    print(min_stones_to_remove(n, s))
