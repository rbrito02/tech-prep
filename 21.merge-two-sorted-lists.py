# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        res = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                if head is None:
                    head = ListNode(list1.val, None)
                    res = head
                else:
                    head.next = ListNode(list1.val, None)
                    head = head.next
                list1 = list1.next
            else:
                if head is None:
                    head = ListNode(list2.val, None)
                    res = head
                else:
                    head.next = ListNode(list2.val, None)
                    head = head.next
                list2 = list2.next

        while list1 is not None:
            if head is None:
                head = ListNode(list1.val, None)
                res = head
            else:
                head.next = ListNode(list1.val, None)
                head = head.next
            list1 = list1.next

        while list2 is not None:
            if head is None:
                head = ListNode(list2.val, None)
                res = head
            else:
                head.next = ListNode(list2.val, None)
                head = head.next
            list2 = list2.next

        return res


# @leet end

# Discussion Board Top Solution
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# dummy.next is the head
#         cur = dummy = ListNode()
# easier way to say is not None
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1, cur = list1.next, list1
#             else:
#                 cur.next = list2
#                 list2, cur = list2.next, list2
#
# if either list still exists
#         if list1 or list2:
# set the rest of that list to cur.next
#             cur.next = list1 if list1 else list2
#
#         return dummy.next

