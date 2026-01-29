class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        rev_str = x_str[::-1]

        if x_str == rev_str:
            print(f"{x_str} reads as {rev_str} from left to right and from right to left")
            return True
        else:
            print(f"From left to right, it reads {x_str}. From right to left, it becomes {rev_str}. Therefore it is not a palindrome")
            return False


            
            