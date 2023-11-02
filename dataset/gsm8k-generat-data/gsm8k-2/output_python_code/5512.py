def solution():
    """An investor invested some money in 2 separate schemes: A and B. Scheme A will yield 30% of the capital within a year, and scheme B will yield 50% of the capital within a year. If he invested $300 in scheme A and $200 in B, how much more money will he have in scheme A than in B after a year, provided he does not withdraw anything?"""
    scheme_a_amount = 300
    scheme_b_amount = 200
    scheme_a_yield = 0.3
    scheme_b_yield = 0.5
    scheme_a_profit = scheme_a_amount * scheme_a_yield
    scheme_b_profit = scheme_b_amount * scheme_b_yield
    difference = scheme_a_profit - scheme_b_profit
    result = difference
    return result

print(solution())