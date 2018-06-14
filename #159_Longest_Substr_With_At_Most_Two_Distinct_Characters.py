class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr_len = 0
        i = 0
        j = 0
        dic = {}
        last_in_dic = ''
        for j in range(len(s)):
            if dic.get(s[j]) == None:
                if len(dic) == 1:
                    last_in_dic = s[j]
                if len(dic) == 2:
                    i = dic[last_in_dic]
                    dic = {}
                    dic[last_in_dic] = i
                    last_in_dic = s[j]
                dic[s[j]] = j
            else:
                if s[j] != last_in_dic:
                    last_in_dic = s[j]
                    dic[s[j]] = j                    
            max_substr_len = max(max_substr_len, j - i + 1)
        return max_substr_len