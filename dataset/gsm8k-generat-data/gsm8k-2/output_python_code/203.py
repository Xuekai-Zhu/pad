def solution():
    """Benny bought 2 soft drinks for $4 each and 5 candy bars. He spent a total of 28 dollars. How much did each candy bar cost?"""
    soft_drinks_cost = 4 * 2
    total_cost = 28
    candy_bars_cost = total_cost - soft_drinks_cost
    candy_bars_count = 5
    candy_bar_price = candy_bars_cost / candy_bars_count
    result = candy_bar_price
    return result

print(solution())