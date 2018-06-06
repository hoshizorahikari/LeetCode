# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from hikari_tool import TreeNode,BinaryTree
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst=[]
        if root is None :
            return lst
        
        stack=[]
        p=root
        while 1:
            while p:
                stack.append(p)
                p=p.left
            if stack:
                p=stack.pop()
                lst.append(p.val)
                p=p.right
            if p is None and stack==[]:
                return lst

        
def main():
    tree=BinaryTree([1,2,3,4,5,6,7,8,9])
    tree.inorder()
    print(Solution().inorderTraversal(tree.root))


if __name__ == '__main__':
    main()
