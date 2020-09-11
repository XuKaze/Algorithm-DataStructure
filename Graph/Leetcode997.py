# find the town judge

'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one \
of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the\
 person labelled a trusts the person labelled b.
If the town judge exists and can be identified, return the label of the town \
judge.  Otherwise, return -1.

Input: N = 2, trust = [[1,2]]
Output: 2
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
'''


def findJudge(N, trust):
    if N == 0: return -1

    graph = {}
    for i in range(1, N+1):
        graph[i] = set()
    for e in trust:
        graph[e[0]].add(e[1])

    print(graph[1])


    candidate = [i for i,v in graph.items() if len(v) == 0]

    if len(candidate) == 0:
        return -1
    candidate = candidate[0]

    for i,v in graph.items():
        if candidate == i:
            continue
        if candidate not in graph[i]:
            return -1
    return candidate


findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
