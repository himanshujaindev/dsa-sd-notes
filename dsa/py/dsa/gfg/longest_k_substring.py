"""
https://www.geeksforgeeks.org/dsa/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
T: O(n)
Even though there's a nested while loop inside the while j < n loop, this is a classic sliding window pattern, so the total work is still linear.

The outer loop advances j from 0 to n-1 — that's n iterations.
The inner while unique > k loop advances i. Crucially, i only ever moves forward, and it can move forward at most n times total across the entire run of the algorithm (it never resets or goes backward).

So across the whole function:

j is incremented at most n times.
i is incremented at most n times.

That gives you O(n) + O(n) = O(2n) = O(n) total, not O(n²). This technique (bounding total inner-loop work across all outer iterations, rather than per-iteration) is called amortized analysis.

S: O(1)
freq is an array of fixed size 26 (for lowercase letters a–z), regardless of the input size n.
"""


def longest_k_substring(s, k):
    # slding window
    i = 0
    j = 0

    n = len(s)
    freq = [0] * 26

    unique = 0  # number of unique characters in the current window
    res = -1

    while j < n:
        pos = ord(s[j]) - ord('a')
        freq[pos] += 1

        if freq[pos] == 1:
            unique += 1

        while unique > k:
            oldPos = ord(s[i]) - ord('a')
            freq[oldPos] -= 1

            if freq[oldPos] == 0:
                unique -= 1

            i += 1

        if unique == k:
            res = max(res, j-i+1)

        j += 1

    return res


s = "eaebc"
k = 2
print(longest_k_substring(s, k))
