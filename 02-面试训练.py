# _*_ coding:utf-8 _*_
# author: zl
# time: 19.09.01
# python: 3.6.2

"""
题目要求：
实现一个带有buildDict, 以及 search方法的魔法字典。
对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。
对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
"""


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.new_list = list()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        self.new_list = dict

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        t = 0         # t表示有几个字母和他不一样

        # 遍历出原文件中的所有单词
        for list_line in self.new_list:
            if len(word) == len(list_line):
                for i in range(len(list_line)):
                    if word[i] == list_line[i]:
                        continue
                    else:
                        t += 1

                if t > 1:
                    continue
                else:
                    print("T")
                    break
            elif len(word) != len(list_line):
                print("F")
                break
        else:
            print("F")


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
obj.buildDict(["hello", "hallo", "leetcode"])   # Output: Null
obj.search("hello")                           # Output: True
obj.search("hhllo")                             # Output: True
obj.search("hell")                           # Output: False
obj.search("leetcoded")                      # Output: False

