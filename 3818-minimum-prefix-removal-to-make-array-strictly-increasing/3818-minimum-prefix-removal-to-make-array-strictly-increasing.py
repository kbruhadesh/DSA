class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        j = n-1

        while j>0 and nums[j-1]<nums[j]:
            j -= 1

        if j == 0:
            return 0

        rem = j
        i=0
        
        while i<j:
            if i > 0 and nums[i] <= nums[i-1]:
                break
            temp=j
            while temp<n and nums[i]>= nums[temp]:
                temp += 1
            if temp < n:
                rem = min(rem,temp)
            i += 1
        return rem
    