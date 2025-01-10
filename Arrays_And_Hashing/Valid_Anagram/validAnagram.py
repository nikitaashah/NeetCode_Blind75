#####################################################################################################################################################
#                                                                                                                                                   #
# Problem Name : Valid Anagram                                                                                                                      #
# Level : Easy                                                                                                                                      #
# Problem Statement: Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.                  #
#                                                                                                                                                   # 
# Example 1:                                                                                                                                        #
# Input: s = "racecar", t = "carrace"                                                                                                               #
# Output: true                                                                                                                                      #
#                                                                                                                                                   #
# Example 2:                                                                                                                                        #
# Input: s = "jar, t = "jam"                                                                                                                        #
# Output: false                                                                                                                                     #
#                                                                                                                                                   #
# Medium article: https://nikitaashah.medium.com/arrays-and-hashing-valid-anagram-python-programming-solution-b98b0ee46540                          #
#                                                                                                                                                   #
#####################################################################################################################################################


######################################
#          Sorting Approach          #
######################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

#####################################################################################################################################################


######################################
#          Initial Approach          #
######################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

#####################################################################################################################################################
