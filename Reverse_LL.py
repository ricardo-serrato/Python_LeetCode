# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    current = head
    prev = None
    n = None

    while current:
        n = current.next
        current.next = prev
        prev = current
        current = n
    head = prev

    return head
