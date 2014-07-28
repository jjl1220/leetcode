class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        # inorder traversal
        st=[]
        inf = 10**10
        low=-inf
        hi=inf
        while root or st:
            if root:
                st.append(root)
                root = root.left
                
            else:
                root = st.pop()
                if not low<root.val<hi: return False
                low=root.val
                hi=inf 
                if len(st)>=2: hi=st[-2].val
                root = root.right
        return True
    