class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        
        #if len(nums1) + len(nums2) == 0:
        #    return 0;
        
        for l1 in xrange(len(nums1)):
            merged.append(nums1[l1])
        for l2 in xrange(len(nums2)):
            merged.append(nums2[l2])
                
        merged.sort()
        
        num = len(merged)
        if (num % 2 == 0):
            # even num/2 and num/2 - 1
            return (merged[num/2] + merged[num/2-1])/2.0
        else:
            return merged[num/2]
            
