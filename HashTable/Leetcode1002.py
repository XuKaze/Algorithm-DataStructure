# 1002. Find Common Characters
'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]

'''
'''
def commonChars(A):
    n = len(A)
    dict = {}
    for i in a:
'''
'''
# My solution WRONG
A = ["bella","label","roller"]
n = len(A)
dict = {}
final_list =[]
for item in A:
    for i in item:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

for item in dict.keys():
    if dict[item] == n:
        final_list.append(item)
    elif dict[item]%n == 0:
        k = dict[item]/n
        for i in range(int(k)):
            final_list.append(item)
    elif dict[item]%n != 0 and dict[item]%n > 1:
'''
# cool solution

from collections import Counter

it = collections.Counter(A[0])

for i in range(2,len(A)):
    num1, num2 = map(Counter, [ A[i-1], A[i]])
    it = it & num1 & num2

print(*it.elements())
