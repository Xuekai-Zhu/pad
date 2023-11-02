def solution():
    """Albert wants a paintbrush that costs $1.50, a set of paints that costs $4.35, and a wooden easel that costs $12.65. Albert already has $6.50. How much more money does Albert need?"""
    total_cost = 1.5 + 4.35 + 12.65
    current_money = 6.5
    remaining_money_needed = total_cost - current_money
    result = remaining_money_needed
    return result

print(solution())