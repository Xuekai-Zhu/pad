def solution():
    """Winston has 14 quarters. He then spends half a dollar on candy. How many cents does he have left?"""
    quarters = 14
    half_dollar = 50
    candy_cost = half_dollar / 2
    total_cents = quarters * 25
    remaining_cents = total_cents - candy_cost
    result = remaining_cents
    return result

print(solution())