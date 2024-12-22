# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, curr_node, height):

        # base case
        # when node does not exist then the height is -1
        if not curr_node:
            return -1

            # logic

        left_height = self.dfs(curr_node.left, height)  # 1
        right_height = self.dfs(curr_node.right, height)  # 1

        # the height for current node
        height = max(left_height, right_height) + 1

        # if that height index does not exist
        # append
        if len(self.ans) == height:
            self.ans.append([curr_node.val])
        # else add it to that height
        else:
            self.ans[height].append(curr_node.val)

        return height

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans
