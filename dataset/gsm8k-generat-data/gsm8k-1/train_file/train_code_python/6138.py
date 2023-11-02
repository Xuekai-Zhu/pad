def solution():
    """Rose is an aspiring artist. She wants a paintbrush that costs $2.40, a set of paints that costs $9.20, and an easel that costs $6.50 so she can do some paintings. Rose already has $7.10. How much more money does Rose need?"""
    paintbrush_cost = 2.40
    paint_set_cost = 9.20
    easel_cost = 6.50
    total_cost = paintbrush_cost + paint_set_cost + easel_cost
    existing_money = 7.10
    remaining_money = total_cost - existing_money
    result = remaining_money
    return result

print(solution())