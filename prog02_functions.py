# A Python DFS program
# to check whether a string C is
# an interleaving of two other
# strings A and B.

# Build 3D array

dp = [[[0] * 101] * 101] * 101
complexity = 0
# This function checks if there exist a valid path from 0,0,0 to s,n,m
# And also check whether the string used both A and B substrings.
def dfs(s, i, j, A, B, C, a, b):
    global complexity
    # Check if the cell is empty.
    if (dp[s][i][j] != -1):
        complexity += 1
        return dp[s][i][j]
    n = len(A)
    m = len(B)
    d = len(C)
    # If there is a path from top the bottom and string A and string B have been used at least once, return True.
    if (s == d):
        complexity += 1
        if a >= n and b >= m:
            complexity += 1
            return 1
        else:
            complexity += 1
            return 0
    # If C[s] matches with both A[i] and B[j]
    # we explore both the paths
    # string A and string B can be repetitively used, a and b would record the true position in 3D matrix.
    if (s < d and i < n and A[i] == C[s] and j < m and B[j] == C[s]):
        complexity += 1
        x = dfs(s + 1, (i + 1) % n, j, A, B, C, a + 1, b)
        y = dfs(s + 1, i, (j + 1) % m, A, B, C, a, b + 1)

        dp[s][i][j] = y | x

        return dp[s][i][j]
    # If C[s] matches with A[i].
    if (s < d and i < n and A[i] == C[s]):
        complexity += 1
        x = dfs(s + 1, (i + 1) % n, j, A, B, C, a + 1, b)

        dp[s][i][j] = x

        return dp[s][i][j]
    # If C[s] matches with B[j].
    if (s < d and j < m and B[j] == C[s]):
        complexity += 1
        y = dfs(s + 1, i, (j + 1) % m, A, B, C, a, b + 1)

        dp[s][i][j] = y

        return dp[s][i][j]
    # if nothing matches we return 0
    dp[s][i][j] = 0
    complexity += 1
    return dp[s][i][j]


# The main function that
# returns true if C is
# an interleaving of A
# and B, otherwise false.
def isInterleaved(A, B, C):
    global complexity
    d = len(C)
    n = len(A)
    m = len(B)

    if (n + m) > d:
        complexity += 1
        return 0
    # initializing 3D array with -1
    for s in range(d + 1):
        for i in range(n + 1):
            for j in range(m + 1):
                dp[s][i][j] = -1

    return dfs(0, 0, 0, A, B, C, 0, 0)


# A function to run test cases
def test(A, B, C):

    result = isInterleaved(A, B, C)
    if (result):
        print(C, "is interleaved of", A, "and", B)

    else:
        print(C, "is not interleaved of", A, "and", B)
    print("time complexity: " + str(complexity))
    print("O(|A|*|B|*|C|) = %i * %i * %i = %i" % (len(A), len(B), len(C), len(A) * len(B) * len(C)))