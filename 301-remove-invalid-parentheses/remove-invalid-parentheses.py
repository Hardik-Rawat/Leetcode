class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            i = 0
            count = 0

            while i < len(string):
                if string[i] == '(':
                    count += 1

                elif string[i] == ')':
                    if count == 0:
                        return False

                    count -= 1

                i += 1

            return count == 0

        level = {s}

        while True:
            valid = list(filter(isValid, level))

            if valid:
                return valid

            level = {
                string[:i] + string[i + 1:]
                for string in level
                for i in range(len(string))
                if string[i] in "()"
            }