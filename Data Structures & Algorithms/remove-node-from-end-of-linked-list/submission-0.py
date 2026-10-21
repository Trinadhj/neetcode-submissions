# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        node_from_start = length-n
        if length == 1:
            return
        length = 0
        curr = prev = head
        while curr:
            if length == node_from_start:
                if curr == head:
                    head = curr.next
                tmp = curr.next
                prev.next = tmp
                return head
            length += 1
            prev = curr
            curr = curr.next
        
