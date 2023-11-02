def solution():
    """John buys 20 candy bars. His brother Dave pays for 6 of them. If each candy bar costs $1.50, how much did John pay?"""
    total_bars = 20
    dave_pays = 6
    john_pays = total_bars - dave_pays
    cost_per_bar = 1.5
    john_cost = john_pays * cost_per_bar
    result = john_cost
    return result

print(solution())