class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # define the return list
        #l = []
        
        # use the dictionary to create a map
        d = {}
        
        # One loop is enough
        # for any element x, check whether any element before x is in the map
        # This way we avoid the issue that dictionary can have collision
        # itself is not in the map yet, so it must be from another node.
        
        for i in xrange(len(nums)):
            
            # if targt -x is in the dictionary; get the index
            if (target-nums[i] in d):
                return (d.get(target-nums[i]), i)

            # add i into the dict here
            d[nums[i]] = i
