class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        b=[False]*len(s)
        ret=0
        for i in range(len(s)):
            if b[i] == False:
                b[i]=True
                if i<len(s)-1:
                    if d[s[i]]<d[s[i+1]]:
                        ret+=d[s[i+1]]-d[s[i]]
                        b[i]=True
                        b[i+1]=True
                    else:
                        ret+=d[s[i]]
                else:
                    ret+=d[s[i]]

        return ret
