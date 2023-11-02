def solution():
    """Rose is an aspiring artist. She wants a paintbrush that costs $2.40, a set of paints that costs $9.20, and an easel that costs $6.50 so she can do some paintings. Rose already has $7.10. How much more money does Rose need?"""
    paintbrush_price = 2.40
    paints_price = 9.20
    easel_price = 6.50
    total_price = paintbrush_price + paints_price + easel_price
    current_money = 7.10
    needed_money = total_price - current_money
    result = needed_money
    return result

print(solution())