# @leet start
class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        for char in s:
            if char == "{" or char == "(" or char == "[":
                st.append(char)
            else:
                if (
                    (char == ")" and (not st or st[-1] != "("))
                    or (char == "}" and (not st or st[-1] != "{"))
                    or (char == "]" and (not st or st[-1] != "["))
                ):
                    return False
                st.pop()

        return not st


# @leet end
