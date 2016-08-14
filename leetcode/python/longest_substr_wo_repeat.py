class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {}
        max = 0; length = 0; pos =0; start = 0
        
        # Start from the beginning, when a character is repeated, stop there
        for c in s:
            if c not in dict:
                length += 1
                if length > max: max = length
            else:
            # if c is in dict, then we should chop the length from where it's started
                dict_pos = dict.get(c)
                if dict_pos >= start:
                    length = pos - dict_pos
                    start = dict_pos + 1
                else:
                    length += 1
                    if length > max: max = length
            dict[c] = pos
            
            # probably there is better way to write it in Python
            pos += 1
            
        return max
