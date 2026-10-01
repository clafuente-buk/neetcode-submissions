class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_dict = {}

        for i in s:
            if string_dict.get(i) is None:
                string_dict[i] = 1
            else:
                string_dict[i] = string_dict[i] + 1
        
        for i in t:
            if string_dict.get(i) is None:
                return False
            else:
                string_dict[i] = string_dict[i] - 1

        for i in string_dict.values():
            if i != 0:
                return False

        return True