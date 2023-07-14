class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ar=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                ar.append(nums[i])
        for i in range(len(ar)):
            nums[i]=ar[i]
        return len(ar)