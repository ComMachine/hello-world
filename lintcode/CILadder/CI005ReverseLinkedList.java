/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
    public ListNode reverse(ListNode head) {
        ListNode p = head;
        ListNode q;
        ListNode r;
        if (head == null) {
            return head;
        }
        q = p.next;
        head.next = null;   // need this to terminate the reversed linked list
        while (p != null) {
            if (q != null) {
                r = q.next;
                q.next = p;
                p = q;
                q = r;
            } else {
                break;
            }
        }
        return p;
    }
}
