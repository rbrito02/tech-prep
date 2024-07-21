# @leet start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = []
        for char in s.lower():
            if char.isalnum():
                newS.append(char)

        print(newS)

        reversed = newS[::-1]
        for idx in range(len(newS)):
            if newS[idx] != reversed[idx]:
                return False

        return True


# @leet end

