# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        curr = head
        while curr is not None:
            if curr in visitedNodes:
                return True
            else:
                visitedNodes.add(curr)
            curr = curr.next
        return False
        
# @leet end
