def solution():
    """Dorothy, Julia, and Robert go to the store to buy school supplies. Dorothy buys half as many pens as Julia. Julia buys three times as many pens as Robert. Robert buys 4 pens. If one pen costs $1.50, how much money did the three friends spend in total on pens?"""
    robert_pens = 4
    julia_pens = robert_pens * 3
    dorothy_pens = julia_pens / 2
    total_pens = robert_pens + julia_pens + dorothy_pens
    pen_cost = 1.5
    total_cost = total_pens * pen_cost
    result = total_cost
    return result

print(solution())