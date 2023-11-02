def solution():
    """Dorothy, Julia, and Robert go to the store to buy school supplies. Dorothy buys half as many pens as Julia. Julia buys three times as many pens as Robert. Robert buys 4 pens. If one pen costs $1.50, how much money did the three friends spend in total on pens?"""
    robert_pens = 4
    julia_pens = 3 * robert_pens
    dorothy_pens = 0.5 * julia_pens
    total_pens = robert_pens + julia_pens + dorothy_pens
    pen_price = 1.5
    total_cost = total_pens * pen_price
    result = total_cost
    return result

print(solution())