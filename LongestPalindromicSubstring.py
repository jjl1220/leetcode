def longestPalindrome(self, s):
    if len(s)==0: return ""
    n = len(s)
    score = [0 for i in range(2*n-1)]
    score[0]=1
    maxindex=0
    for i in range(1,n):
        start=i-1; end=i
        while start>=0 and end<n and s[start]==s[end]:
            start-=1
            end+=1
            score[2*i-1]+=2
        if score[2*i-1]>score[maxindex]: maxindex = 2*i-1
        
        score[2*i]=1
        start=i-1; end=i+1
        while start>=0 and end<n and s[start]==s[end]:
            start-=1; end+=1
            score[2*i]+=2
        if score[2*i]>score[maxindex]: maxindex=2*i
    leng = score[maxindex]
    if maxindex%2==1: return s[maxindex/2-leng/2+1:maxindex/2+leng/2+1]
    else: return s[maxindex/2-leng/2: maxindex/2+leng/2+1]


