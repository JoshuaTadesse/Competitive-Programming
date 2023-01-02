import copy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        for i, en in enumerate(nums):
            rem = target - nums[i]
            
            if rem in array:
                return [i, array[rem]]
            array[en] = i