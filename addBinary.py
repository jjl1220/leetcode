class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res=''
        ia=len(a)-1
        ib=len(b)-1
        carry=0
        while ia>=0 or ib>=0 or carry>0:
            s=0
            if ia>=0: s+=int(a[ia])
            if ib>=0: s+=int(b[ib])
            if carry>0: s+=carry
            carry =s/2
            res+=str(s%2)
            ia-=1; ib-=1
        return res[::-1]