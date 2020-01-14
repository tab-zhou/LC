"""
题目：返回任意字符串中最长的回文字符串
思路：一、暴力法，在初始字符串中遍历长度N-i的回文字符串 T(n)=O(n**2)
     二、双指针，回文字符串有两种形态，aba和abba，都是以中心向两边发散，所以只要移动中心位置不断发散便可找出以当前位置最长的回文字符串T(n)=O(n*log(n))
"""


class LongestPalindromicString(object):

    @staticmethod
    def is_palindromic_string(or_string):
        if or_string == or_string[::-1]:
            return True
        else:
            return False

    @staticmethod
    def get_sub_string(or_string):
        longest_palindromic_string = []
        length = len(longest_palindromic_string)
        for index in range(0, len(or_string)):
            for half_len in range(0, min(index+1, len(or_string)-index+1)):
                if LongestPalindromicString.is_palindromic_string(or_string[index-half_len:index+half_len+1:]):
                    if length < len(or_string[index - half_len:index + half_len + 1:]):
                        length = len(or_string[index - half_len:index + half_len + 1:])
                        longest_palindromic_string = or_string[index - half_len:index + half_len + 1:]
                elif LongestPalindromicString.is_palindromic_string(or_string[index-half_len:index+half_len:]):
                    if length < len(or_string[index - half_len:index + half_len:]):
                        length = len(or_string[index - half_len:index + half_len:])
                        longest_palindromic_string = or_string[index - half_len:index + half_len:]
                else:
                    break

        return longest_palindromic_string


test_suite = ['aa123', '', 'abcdd', 'aaaaa', 'abcddd']
for test_case in test_suite:
    print(LongestPalindromicString.get_sub_string(test_case))

