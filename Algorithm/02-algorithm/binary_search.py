from typing import List

# Example 1:
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# Example 2:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            temp = nums[mid]

            if temp == target:
                return mid

            if temp > target:
                high = mid - 1
            else:
                low = mid + 1

        return None