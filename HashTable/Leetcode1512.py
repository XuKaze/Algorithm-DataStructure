# Task
'''
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
# Solutioon 1
from collections import Counter
def numIdenticalPairs(nums):
    num_counter = Counter()
    for num in nums:
        num_counter[num]+=1
    good_pair_count = 0
    for n in num_counter.values():
        good_pair_count += n*(n-1)/2
    return int(good_pair_count)
