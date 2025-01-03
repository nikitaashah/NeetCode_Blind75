#####################################################################################################################################################
#                                                                                                                                                   #
# Problem Name : Contains Duplicate                                                                                                                 #
# Level : Easy                                                                                                                                      #
# Problem Statement: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.             #
#                                                                                                                                                   # 
# Example 1:                                                                                                                                        #
# Input: nums = [1, 2, 3, 3]                                                                                                                        #
# Output: true                                                                                                                                      #
#                                                                                                                                                   #
# Example 2:                                                                                                                                        #
# Input: nums = [1, 2, 3, 4]                                                                                                                        #
# Output: false                                                                                                                                     #
#                                                                                                                                                   #
# Medium article: https://nikitaashah.medium.com/arrays-and-hashing-contains-duplicate-python-programming-solution-3591951a45f9                     #
#                                                                                                                                                   #
#####################################################################################################################################################


##############################################
#          Hash Set Length Approach          #
##############################################

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

#####################################################################################################################################################


#######################################
#          Hash Set Approach          #
#######################################

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

#####################################################################################################################################################


######################################
#          Sorting Approach          #
######################################

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

#####################################################################################################################################################


##########################################
#          Brute Force Approach          #
##########################################

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

#####################################################################################################################################################


######################################
#          Initial Approach          #
######################################

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 1
        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i + 1]:
                count += 1
                i += 1
            else:
                i += 1
        if count > 1:
            return True
        else:
            return False

#####################################################################################################################################################
