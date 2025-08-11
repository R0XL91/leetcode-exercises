# Solution for problem: 1768 Merge Strings Alternately (Easy)

from typing import *


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Complexity: O( m + n ) -> We iterate through the characters of both words.
        # Space Complexity: O( m + n ) -> We are using a list to store the result.
        word1_len, word2_len = len(word1), len(word2)
        min_word = min(word1_len, word2_len)
        result = []
        for index in range(min_word):
            result.append(word1[index])
            result.append(word2[index])
        if word1_len > min_word:
            result.append(word1[min_word:])
        elif word2_len > min_word:
            result.append(word2[min_word:])
        return "".join(result)

    def best_solution_merge_strings_alternately(self, word1: str, word2: str) -> str:
        # Solution from LeetCode
        # Complexity: O( m + n ) -> We iterate through the characters of both words.
        # Space Complexity: O( m + n ) -> We are using a list to store the result.
        m, n = len(word1), len(word2)
        i, j = 0, 0
        result = []
        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1
        return "".join(result)
