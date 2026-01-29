class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7

        cont = [0] * 26
        for char in s:
            cont[ord(char) - ord('a')] += 1

        for _ in range(t):
            new_cont = [0] * 26

            
            for i in range(25):
                new_cont[i + 1] = (new_cont[i + 1] + cont[i]) % mod

            
            new_cont[0] = (new_cont[0] + cont[25]) % mod
            new_cont[1] = (new_cont[1] + cont[25]) % mod

            cont = new_cont

        return sum(cont) % mod
