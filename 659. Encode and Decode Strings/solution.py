# Solution using simple string operations
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs: 
            ans += str(len(word)) + '#' + word 
        return ans

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#': 
                j += 1
            length = int(s[i:j])
            res.append(str(s[j+1 : j+1+length]))
            i = j + 1 + length
        return res
