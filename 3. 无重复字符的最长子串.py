"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

哈希表，双指针，字符串
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        max_len = 0
        start = 0  # 记录不重复字符串首位
        d = {}  # 每个字符为key, 下标为value
        for i in range(len(s)):
            # 如果s[i]在start~i不重复(0~i不重复或重复位置<start), 随时更新最大长度
            if s[i] not in d or d[s[i]] < start:
                max_len = max(max_len, i - start + 1)
            else:  # 重复则start移到与s[i]重复字符后一位
                start = d[s[i]] + 1
            d[s[i]] = i  # 更新字符对应下标
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))  # 3
    print(s.lengthOfLongestSubstring('bbbbb'))  # 1
    print(s.lengthOfLongestSubstring('pwwkew'))  # 3
    print(s.lengthOfLongestSubstring('aab'))  # 2
    print(s.lengthOfLongestSubstring('abb'))  # 2
    print(s.lengthOfLongestSubstring('dedf'))  # 3
    print(s.lengthOfLongestSubstring('abba'))  # 2
