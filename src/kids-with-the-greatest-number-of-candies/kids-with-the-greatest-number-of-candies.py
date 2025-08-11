# Solution for problem: 1431 Kids With the Greatest Number of Candies (Easy)

from typing import List


class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Complexitiy: O(n) -> We iterate through the list of candies once to find the maximum and then again to check each kid.
        # Space Complexity: O(n) -> We are using a list to store the results.
        max_kid_candy = max(candies)
        return [kid_candy + extraCandies >= max_kid_candy for kid_candy in candies]

    def best_solution_kids_with_candies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Solution from LeetCode
        # Complexity: O(n) -> We iterate through the list of candies once to find the maximum and then again to check each kid.
        # Space Complexity: O(1) -> Without counting the space of input and output, we are not using any space except for some integers like maxCandies and candy
        # For this space complexity we are overwriting the result list in place, that's the reason we are not counting it.
        # This solution is more memory efficient as it does not create a new list for the result
        maxCandies = max(candies)
        result = []
        for index, __ in enumerate(candies):
            result.append(candies[index] + extraCandies >= maxCandies)
        return result
