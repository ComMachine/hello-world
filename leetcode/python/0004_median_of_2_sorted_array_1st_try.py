class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Recursive algorithm, 
        len1 = len(nums1)
        len2 = len(nums2)
        mlist = []
        
        # to end the recursion
        if len1 == 1 and len2 == 1:
            return float(nums1[0]+nums2[0])/2
            
        if len1 == 1 and len2 == 2:
            mlist.append(nums1[0])
            mlist.append(nums2[0])
            mlist.append(nums2[1])
            mlist.sort()
            return mlist[1]
        
        if len1 == 2 and len2 == 1:
            mlist.append(nums1[0])
            mlist.append(nums1[1])
            mlist.append(nums2[0])
            mlist.sort()
            return mlist[1]
        
        if len1%2 == 0 and len2%2 ==0:
            if (nums1[len1/2] < nums2[len2/2-1]):
                return self.findMedianSortedArrays(nums1[len1/2:], nums2[:len2/2-1+1])

            if (nums2[len2/2] < nums1[len1/2-1]):
                return self.findMedianSortedArrays(self, nums2[len2/2:], nums1[:len1/2-1+1])                
            
            mlist.append(nums1[len1/2-1])
            mlist.append(nums2[len2/2-1])
            mlist.append(nums2[len2/2])
            mlist.append(nums1[len1/2])
            mlist.sort()
            return float(mlist[1]+mlist[2])/2

        if len1%2 == 1 and len2%2 == 1:
            if (nums1[len1/2] == nums2[len2/2]):
                return nums1[len1/2]
            if (nums1[len1/2] < nums2[len2/2]):
                return self.findMedianSortedArrays(self, nums1[len1/2:], nums2[:len2/2+1])
            if (nums1[len1/2] > nums2[len2/2]):
                return self.findMedianSortedArrays(self, nums2[len2/2:], nums1[:len1/2+1])
                
        if len1%2 == 1 and len2%2 == 0:
            if (nums1[len1/2] >= nums2[len2/2-1] and nums1[len1/2] <= nums2[len2/2]):
                return nums1[len1/2]
            if (nums1[len1/2] < nums2[len2/2-1]):
                return self.findMedianSortedArrays(self, nums1[len1/2:], nums2[:len2/2-1+1])
            if (nums1[len1/2] > nums2[len2/2-1]):
                return self.findMedianSortedArrays(self, nums2[len2/2-1:], nums1[:len1/2+1])               

        if len1%2 == 0 and len2%2 == 1:
            if (nums2[len2/2] >= nums1[len1/2-1] and nums1[len1/2] <= nums1[len1/2]):
                return nums2[len2/2]
            if (nums2[len2/2] < nums1[len1/2-1]):
                return self.findMedianSortedArrays(self, nums2[len2/2:], nums1[:len1/2-1+1])
            if (nums2[len2/2] > nums1[len1/2-1]):
                return self.findMedianSortedArrays(self, nums1[len1/2-1:], nums2[:len2/2+1])   
