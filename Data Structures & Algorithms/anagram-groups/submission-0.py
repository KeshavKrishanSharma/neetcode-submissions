class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # for a in strs:
        #    k="".join(sorted(a))
        #    if k not in p:
        #         p[k]=[]
                
        #    p[k].append(a)
        # return list(p.value())
        p = defaultdict(list)

        for a in strs:
            count = [0] * 26

            for ch in a:
                count[ord(ch) - ord('a')] += 1

            p[tuple(count)].append(a)

        return list(p.values())
