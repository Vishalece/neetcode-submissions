# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head == None or head.next == None):
            return
        
        slow = head
        fast = head
        first = head
        while(fast != None and fast.next != None):
            slow =  slow.next
            fast = fast.next.next
        
        sec = slow.next
        slow.next = None

        prev = None
        curr = sec
        while(curr != None):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        sec = prev
        
        while(sec != None):
            l1 = first.next
            l2 = sec.next

            first.next = sec
            sec.next = l1

            first = l1
            sec = l2






            
        



