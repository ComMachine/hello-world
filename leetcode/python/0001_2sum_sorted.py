class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # define the return list
        l = []
        
        # sort the list
        # Note that the subscripts changed in the sorted array
        # sorted() will generate a new sorted list
        sortednums = sorted(nums)
        
        # move two points from both sides to see whether we can find the target
        # there is only one target in the solution
        # Prove: x + y < t if y'>y =>because that's why we move y' to y.
        #                     x'<x, x'+y'>t, so x+y'>t 

        i = 0
        j = len(sortednums)-1
        #while (i<len(sortednums)):
        #    while (j>0):
        # This is more optimized
        while (i < j):
                # found the numbers; go find the original subscripts
                if (sortednums[i]+sortednums[j] == target):
                    # here there is a caveat that when sortednums[i] == sortednums[j]
                    # index() will only locate first number so it will generate the same index
                    # enumerate() is useful here
                    # Another way: Search the smaller from the left and search the larger from the right
                    count = 0
                    for idx, val in enumerate(nums):
                        if (val == sortednums[i]):
                            l.append(idx)
                            count = count + 1
                        # another caveat: need to use else otherwise when sortednums[i] == sortednums[j]
                        # the index was added twice and the output will be doubled.
                        elif (val == sortednums[j]):
                            l.append(idx)
                            count = count + 1
                            # Wrong optimization; break when the larger number is found
                            # we are enumerating the original list and it's not sorted
                            #if (sortednums[i] != sortednums[j]):
                            #    break
                        # Correct optimization: corrected two numbers only
                        if (count == 2):
                            break
                    return l
                
                # move the lower pointer
                if (sortednums[i]+sortednums[j] < target):
                    i = i+1
                    #if (i == j):
                    #    break
                    continue
                
                # move the higher pointer
                if (sortednums[i]+sortednums[j] > target):
                    j = j-1
                    #if (i == j):
                    #    break
                    continue
                
                    
