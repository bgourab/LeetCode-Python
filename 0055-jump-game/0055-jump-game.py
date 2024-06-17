class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j= len(nums)-1
        
        for i in range(len(nums)-1, -1,-1):
            if i + nums[i] >= j:
                j = i
        
        return True if j==0 else False