#Time Complexity:: O(n)-all nodes are visited once
#Space Complexity:: O(n)-extra space used to create a list of nodes in each level
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: #edge case
            return []
        
        result=[] #array to store each level
        q=deque() 
        q.append(root) #pushing the root node into the q
        
        while q: #while q is not empty
            size = len(q) #the length of the q as the number nodes in q may vary
            level=[] #to hold the nodes in each level
            
            for i in range(size): #for loop to process each level
                node = q.popleft() #popping nodes from the front of the q
                level.append(node.val) #appending the popped nodes value into the level list
                
                if node.left: #if the nodes left isn't null then push into q so we can continue traversal
                    q.append(node.left)
                if node.right:
                    q.append(node.right) #if the nodes right isn't null then push into q so we can continue traversal
            result.append(level) #each level is appended as a list into the result
        return result