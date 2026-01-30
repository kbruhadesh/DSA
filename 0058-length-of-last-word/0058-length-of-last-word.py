class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last_word = ""

        for ch in s[::-1]:
            if ch == " ":
                break
            last_word += ch

        return len(last_word)
