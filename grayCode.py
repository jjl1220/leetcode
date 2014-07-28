class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res=[0]
        for i in range(n):
            half = [2**i+num for num in res[::-1]]
            res=res + half
        return res
        
        