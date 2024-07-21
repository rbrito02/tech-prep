# @leet start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for idx, num in enumerate(nums):
            if target - num in complements:
                return [complements[target - num], idx]
            else:
                complements.update({num: idx})

        return []


# @leet end

