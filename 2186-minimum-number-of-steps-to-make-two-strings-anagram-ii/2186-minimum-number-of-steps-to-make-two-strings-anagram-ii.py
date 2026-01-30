class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0]*26
        

        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in t:
            freq[ord(char)- ord('a')] -= 1

        steps = sum(abs(x) for x in freq)
        return steps

        return steps