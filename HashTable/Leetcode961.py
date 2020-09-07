# 961. N-Repeated Element in Size 2N Array

'''
In a array A of size 2N, there are N+1 unique elements,
and exactly one of these elements is repeated N times.

Return the element repeated N times.
Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2
'''
# my solution
def repeatedNTimes(A):
    n = len(A)/2
    for i in A:
        if n == A.count(i):
            return i

# hashmap
def repeatedNTimes(A):
    dict = {}
    n = len(A)
    for i in range(A):
        if A[i] not in dict:
            dict[a[i]] = 1
        else:
            return A[i]
