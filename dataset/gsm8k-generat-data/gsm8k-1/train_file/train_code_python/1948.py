def solution():
    """Albert wants a paintbrush that costs $1.50, a set of paints that costs $4.35, and a wooden easel that costs $12.65.
    Albert already has $6.50. How much more money does Albert need?"""
    paintbrush_cost = 1.5
    paints_cost = 4.35
    easel_cost = 12.65
    total_cost = paintbrush_cost + paints_cost + easel_cost
    money_available = 6.5
    money_needed = total_cost - money_available
    result = money_needed
    return result

print(solution())