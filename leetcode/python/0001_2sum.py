class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = []
        
        for i in xrange(0, len(nums)):
            for j in xrange (i+1, len(nums)):
            # no need to handle the special case that i==j, can start from i+1
            #for j in xrange(0, len(nums)):
                #if (i==j):
                #    continue
                if (nums[i]+nums[j] == target):
                    #l.append(i)
                    #l.append(j)
                    #return l
                    # this can be one line
                    return (i, j)
