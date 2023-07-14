class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret=""
        shrtstStr = ""
        minLn=300 #len(strs[0])
        for s in strs:
            n=len(s)
            if n<minLn:
                minLn=n
                shrtstStr=s
                
        for i in range(minLn):
            for s in strs:
                if s[i]!=shrtstStr[i]:
                    return ret
            ret+=s[i]
            
        return ret