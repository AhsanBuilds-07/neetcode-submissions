
class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_string = ""

        # Remove spaces and special characters
        for ch in s:
            if ch.isalnum():
                new_string += ch.lower()

        # Initialize two pointers
        left = 0
        right = len(new_string) - 1

        # Compare characters
        while left < right:

            if new_string[left] != new_string[right]:
                return False

            left += 1
            right -= 1

        return True
