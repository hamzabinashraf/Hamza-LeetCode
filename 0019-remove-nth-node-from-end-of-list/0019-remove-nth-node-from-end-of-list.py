# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp is not None:
            temp = temp.next
            size += 1
        if n == size:
            head = head.next
            return head
        i = 1
        findpos = size - n
        prev = head
        while i < findpos:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head