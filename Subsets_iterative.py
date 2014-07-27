class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        res=[[]]
        for depth in reversed(range(len(S))):
            if depth==0 or S[depth]!=S[depth-1]:
                res+=res
                for j in range(len(res)/2):
                    res[j]=[S[depth]]+res[j]
            else:
                for j in range(len(res)):
                    res[j]=[S[depth]]+res[j]
        return res
        