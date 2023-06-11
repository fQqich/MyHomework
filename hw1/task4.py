from typing import List

nums = [6, 2, 3, 20, 13]

k = 3

def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    result = 0
    while k>0:
        Maximum = max(nums)
        result = result + Maximum
        nums.remove(Maximum)
        k -= 1
    return result