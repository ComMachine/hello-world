class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {} # dict can be a simply hash of ASCII code
        max = 0; length = 0; start = 0
        repeat_found = False #introducig this boolean seems to help me understand the flow, probably could merge the two ifs in C but Python doesn't support (dict_pos = dict.get(c))>=start in if
        
        # Start from the beginning, when a character is repeated, stop there
        for pos, c in enumerate(s):
            # only c is in dict and beyond the start it counts
            # no need to clear the dict by introducing this start variable
            if c in dict:
                dict_pos = dict.get(c)
                if dict_pos >= start:
                    repeat_found = True
            
            if repeat_found:
                # if c is in dict, then we should chop the length from where it's started
                # always smaller than max by definition because on repeat was found
                length = pos - dict_pos
                start = dict_pos + 1
                repeat_found = False
            else:
                length += 1
                if length > max: max = length
            dict[c] = pos # very important step, update the latest appearance
            
        return max
