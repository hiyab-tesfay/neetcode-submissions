# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            node1 = pq.popleft()
            node2 = qq.popleft()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False

            pq.append(node1.left)
            qq.append(node2.left)
            pq.append(node1.right)
            qq.append(node2.right)

        return True
