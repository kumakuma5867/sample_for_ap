from typing import List
from itertools import combinations


def solve_brute_force(n: int, W: int, weight: List[int], value: List[int]) -> int:
    """
    Solve by simple brute force logic.
    This algorithm is probably correct but quantity of calculations will burst.
    This function should NOT be used.
    """
    mapped_items = [{"w": w, "v": v} for i, (w, v) in enumerate(zip(weight, value))]

    maximum_value: int = 0
    updated: bool = False
    for i in range(1, n + 1):
        if i > 1 and not updated:
            break

        updated = False
        for chosen_items in list(combinations(mapped_items, i)):
            sum_weight = 0
            sum_value = 0
            for item in chosen_items:
                sum_weight += item["w"]
                sum_value += item["v"]

            if sum_weight <= W and maximum_value < sum_value:
                updated = True
                maximum_value = sum_value
    return maximum_value


def solve_dp(n: int, W: int, weight: List[int], value: List[int]) -> int:
    """
    Solve by dynamic planing.
    This algorithm create matrix which row means count of selection and column means total weight.
    While selecting item one by one, determin if items are selectable at the same time and
    if items should be replaced.
    This is much faster than brute force.
    """
    dp = [[0] * (W + 1) for i in range(n + 1)]

    for i, (w, v) in enumerate(zip(weight, value)):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]
            if j - w >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)

    return dp[n][W]
