def solution():
    """Yanna bought ten shirts at $5 each and three pairs of sandals at $3 each. How much change did she get back if she gave a one hundred dollar bill?"""
    shirts_cost = 10 * 5
    sandals_cost = 3 * 3
    total_cost = shirts_cost + sandals_cost
    change = 100 - total_cost
    result = change
    return result

print(solution())