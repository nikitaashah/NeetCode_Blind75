#####################################################################################################################################################
#                                                                                                                                                   #
# Problem Name : Two Sum                                                                                                                            #
# Level : Easy                                                                                                                                      #
# Problem Statement: Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target        #
#                    and i != j. You may assume that every input has exactly one pair of indices i and j that satisfy the condition. Return         # 
#                    the answer with the smaller index first.                                                                                       #
#                                                                                                                                                   # 
# Example 1:                                                                                                                                        #
# Input: nums = [3, 4, 5, 6], target = 7                                                                                                            #
# Output: [0, 1]                                                                                                                                    #
#                                                                                                                                                   #
# Example 2:                                                                                                                                        #
# Input: nums = [4, 5, 6], target = 10                                                                                                              #
# Output: [0, 2]                                                                                                                                    #
#                                                                                                                                                   #
# Example 3:                                                                                                                                        #
# Input: nums = [5, 5], target = 10                                                                                                                 #
# Output: [0, 1]                                                                                                                                    #
#                                                                                                                                                   #
# Medium article: https://medium.com/@nikitaashah/arrays-and-hashing-two-sum-python-programming-solution-1af9f3aa82dc                               #
#                                                                                                                                                   #
#####################################################################################################################################################


##################################################
#          Hash Map Approach (Two Pass)          #
##################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]


#####################################################################################################################################################


######################################
#          Sorting Approach          #
######################################


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()

        i, j = 0, len(nums) - 1

        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []


#####################################################################################################################################################


##########################################
#          Brute Force Approach          #
##########################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

#####################################################################################################################################################


#######################################
#           Initial Approach          #
#######################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums[i + 1:]:
                return [i, nums.index(temp)]

####################################################################################################################################################
