class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = collections.defaultdict()
        for index, ele in enumerate(nums):
            if target - ele in map:
                return [map[target-ele], index]
            
            map[ele] = index
        