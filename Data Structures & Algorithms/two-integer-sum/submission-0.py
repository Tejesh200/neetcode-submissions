class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict  = {}
        for num in range(len(nums)):
            key = target-nums[num]
            if key in dict:
                return[dict[key],num]
            else:
                dict[nums[num]] = num

