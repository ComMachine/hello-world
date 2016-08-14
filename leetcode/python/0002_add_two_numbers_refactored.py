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
        # Create a dummy node (for list operation)
        l = ListNode(0)
        tail = l
        
        while (p != None or q != None):
            
            p_val = 0 if (p == None) else p.val
            q_val = 0 if (q == None) else q.val
            
            if (p != None): p = p.next
            if (q != None): q = q.next
    
            n = ListNode((p_val + q_val + carry) % 10)
            
            tail.next = n
            tail = n

            carry = (p_val + q_val + carry)/10
            
        if (carry > 0):
            n = ListNode(1)
            tail.next = n
            tail = n
            
        return l.next
