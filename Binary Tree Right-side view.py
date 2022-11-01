#BFS
#Time Complexity:: O(n)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(n)-a result array is required to store all rightmost nodes in each level
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
            
        result=[]
        q = deque() #nodes go in the queue
        q.append(root)

        while q: #each time a node is popped from the q, it's children are pushed into q
            size = len(q)
            
            for e in range(size):
                node = q.popleft() #popping first element from queue
                #Both left and right nodes are pushed into q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(node.val) #the last popped nodes value from queue is node.val, which always going to be rightmost node in each level
            
        return result #returning a list of rightmost nodes in each level