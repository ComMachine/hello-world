# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        p = l1
        q = l2
        carry = 0
        
        # list to return
        l = None
        tail = None
        
        # this way I mixed two cases, it's not very straightforward
        # maybe I should traverse to the end of both lists first
        while (p != None or q != None):
            
            p_val = 0
            q_val = 0
            # See the complex cases here?
            if (p != None):
                p_val = p.val
                p = p.next
            if (q != None):
                q_val = q.val
                q = q.next
    
            n = ListNode((p_val + q_val + carry) % 10)
            
            # set return list
            # The insertion should be helped with a dummy node, which I had
            # but removed. l = ListNode(0) at one time
            if (l == None):
                l = n

            if (tail != None):
                tail.next = n
            tail = n
            if (p_val + q_val + carry >= 10):
                carry = 1
            else:
                carry = 0
            
        if (carry > 0):
            n = ListNode(1)
            if (tail != None):
                tail.next = n
            if (l == None):
                l = n
            
        return l
