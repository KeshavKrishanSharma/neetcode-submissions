class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # for a in s:
        #     if s.count(a) != t.count(a):
        #         return False

        # return True

        count = [0] *26

        for a,b in zip(s,t):
            count[ord(a)-ord('a')] += 1
            count[ord(b)-ord('a')] -= 1
        
        return all(x==0 for x in count)