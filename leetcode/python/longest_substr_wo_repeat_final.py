class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # sliding window [i,j). i is the left side aka start
        # j is the current
        start = 0; ans=0; dict={}
        dict = {} # dict can be a simply hash of ASCII code

        for pos, c in enumerate(s):
            if (c in dict):
                start = max(dict.get(c), start)  # using the max function simplied the math for start
            ans = max(ans, pos-start+1)  # here also don't keep the length++, calculate it every time
            dict[c] = pos+1  # implicitly set the new start
            
        return ans
