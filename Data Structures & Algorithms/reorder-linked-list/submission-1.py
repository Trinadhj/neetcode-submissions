# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the linkedlist

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None

        #reverse the second half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merge two halfes
        second = prev
        curr = head
        while second:
            tmp1, tmp2 = curr.next, second.next
            curr.next = second
            second.next = tmp1
            curr, second = tmp1, tmp2
        