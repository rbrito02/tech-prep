# @leet start
class Solution:
    def isValid(self, s: str) -> bool:

        st = []  # Creates Stack

        for char in s:
            if char == "{" or char == "(" or char == "[":
                st.append(char)
            else:
                if (
                    # if stack isnt empty and top element doesnt match
                    (char == ")" and (not st or st[-1] != "("))
                    or (char == "}" and (not st or st[-1] != "{"))
                    or (char == "]" and (not st or st[-1] != "["))
                ):
                    return False
                st.pop()

        # return stack.empty()
        return not st


# @leet end
