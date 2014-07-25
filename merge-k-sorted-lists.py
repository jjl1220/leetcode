class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def merge(self, l1,l2):
        dummy=ListNode(0)
        p=dummy
        while l1 and l2:
            if l1.val<l2.val:
               p.next=l1
               l1,p=l1.next,p.next
            else:
                p.next=ListNode(l2.val)
                l2=l2.next; p=p.next
        if l1==None: p.next = l2
        if l2==None: p.next = l1
        return dummy.next
        
    def mergeKLists(self, lists):
        if len(lists)==0: return None
        if len(lists)==1: return lists[0]
        if len(lists)==2: return self.merge(lists[0],lists[1])
        return self.merge(self.mergeKLists(lists[:len(lists)/2+1]),self.mergeKLists(lists[len(lists)/2+1:]))