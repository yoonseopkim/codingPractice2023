# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSametree(root,subRoot):
            return True
        if not root:
            return False
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
            return True

    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return p.val == q. val and self.isSametree(q.left,p.left) and self.isSametree(q.right,p.right)
