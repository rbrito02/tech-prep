# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.swap(root, root.left, root.right)
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

    def swap(
        self,
        root: Optional[TreeNode],
        node1: Optional[TreeNode],
        node2: Optional[TreeNode],
    ):
        temp = node1
        node1 = node2
        node2 = temp
        root.left, root.right = node1, node2


# @leet end

