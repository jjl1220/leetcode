class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        pre=ListNode(0)
        pre.next=head
        start=pre
        for i in range(m-1): start=start.next
        tail=start.next
        for ct in range(n-m):
            tmp=tail.next
            tail.next=tmp.next
            tmp.next=start.next
            start.next=tmp
        return pre.next