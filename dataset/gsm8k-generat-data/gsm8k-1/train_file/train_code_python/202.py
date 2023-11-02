def solution():
    """Benny bought 2 soft drinks for $4 each and 5 candy bars. He spent a total of 28 dollars. How much did each candy bar cost?"""
    soft_drinks_cost = 4 * 2
    total_cost = 28
    candy_bars_cost = total_cost - soft_drinks_cost
    num_candy_bars = 5
    cost_per_candy_bar = candy_bars_cost / num_candy_bars
    result = cost_per_candy_bar
    return result

print(solution())