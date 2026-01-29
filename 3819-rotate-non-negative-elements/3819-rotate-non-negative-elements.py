class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        temp = nums[:]
        arr = deque([x for x in nums if x>=0])
        if not arr:
            return nums

        k %= len(arr)
        arr.rotate(-k)
        idx=0

        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=arr[idx]
                idx+=1
        return nums
        