#!/usr/bin/env python3

# 53. Given an integer array nums,
# find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Algorithm: Divide and Conquer

# left maximum subarry sum of a given list nums[]
def left_maxsum(nums):
    curr_sum = 0
    left_subsum = float('-inf')
    for i in range(len(nums)//2, -1, -1):
        curr_sum += nums[i]
        left_subsum = max(left_subsum, curr_sum)
    return left_subsum

# right maximum subarry sum of a given list nums[]
def right_maxsum(nums):
    curr_sum = 0
    right_subsum = float('-inf')
    for i in range(len(nums)//2+1, len(nums)):
        curr_sum += nums[i]
        right_subsum = max(right_subsum, curr_sum)
    return right_subsum

# cross maximum subarry sum of a given list nums[] based on previous functions 
def cross_maxsum(nums):
    left = left_maxsum(nums)
    right = right_maxsum(nums)
    return left + right   

if __name__ == "__main__":
    test_list = [-2,1,-3,4,-1,2,1,-5,4]
    # test_list = [1]
    # test_list = [0]
    # test_list = [-1]
    # test_list = [-100000]

    # base case
    if len(test_list) == 1:
        print(test_list[0])
    else:
        l = left_maxsum(test_list)
        r = right_maxsum(test_list)
        c = cross_maxsum(test_list)
        print(max(l, r, c))
