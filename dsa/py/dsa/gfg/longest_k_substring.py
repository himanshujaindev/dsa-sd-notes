"""
https://www.geeksforgeeks.org/dsa/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
T: O(n)
Even though there's a nested while loop inside the outer while loop, this is not O(n²). Here's why:

The outer pointer j moves from 0 to n-1 exactly once → n steps total.
The inner pointer i only ever moves forward (it never resets or decreases). Across the entire execution, i can advance at most n times total, since it's bounded by j.

So even though the inner loop is written inside the outer loop, the total work done by both pointers combined is O(n) + O(n) = O(n). This is the classic two-pointer / sliding window amortized analysis — each element is added to the window once (by j) and removed at most once (by i).


S: O(1)
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
