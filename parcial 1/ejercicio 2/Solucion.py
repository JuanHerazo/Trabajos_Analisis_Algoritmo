#CONTAINS DUPLICATE
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Complejidad tiempo: O(n)
#Complejidad tiempo: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    vistos = set()
    for x in nums:
        if x in vistos:
            return True
        vistos.add(x)
    return False

print(containsDuplicate([1,2,3,4])) #poner aca el TEST CASE
    #[1,2,3,1] TEST CASE 1 - TRUE
    #[1,2,3,4] TEST CASE 2 - FALSE
    #[1,1,1,3,3,4,3,2,4,2] TEST CASE 3 - TRUE