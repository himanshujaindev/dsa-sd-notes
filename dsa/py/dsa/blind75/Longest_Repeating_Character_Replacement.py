# https://leetcode.com/problems/longest-repeating-character-replacement/

"""
Logic:
- Replace less frequent char in a given window
- Use sliding window
- Valid window: (windowLen - count(mostFreqChar) <= k)

T: O(2n * 26) = O(n)
S: O(26) = O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = dict()
        l = 0
        res = 0

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)

            # valid windown
            while (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


if __name__ == "__main__":
    sc = Solution()
    res = sc.characterReplacement("ABABBA", 2)
    print(res)
