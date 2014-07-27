class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def dfs(self,S,depth):
        if depth==len(S): return [[]]
        res=[]
        for j in self.dfs(S,depth+1):
            res.append([S[depth]]+j)
            if depth==0 or S[depth]!=S[depth-1]:
                res.append(j)
        return res
    def subsets(self, S):
        S.sort()
        return self.dfs(S,0)
        
        
        