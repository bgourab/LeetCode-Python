class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force Approach o(n^2)
        '''for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return ([i,j])'''
        # HashMap/Dictionary approach o(n)
        VisitedMap={} # val:index
        for index,num in enumerate(nums):
            difference = target-num
            if difference in VisitedMap:
                return (VisitedMap[difference],index)
            VisitedMap[num]=index
        return