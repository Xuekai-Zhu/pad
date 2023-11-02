def solution():
    """Dorothy, Julia, and Robert go to the store to buy school supplies. Dorothy buys half as many pens as Julia. Julia buys three times as many pens as Robert. Robert buys 4 pens. If one pen costs $1.50, how much money did the three friends spend in total on pens?"""
    # Define the cost per pen
    cost_per_pen = 1.5

    # Calculate the number of pens each person bought
    robert_pens = 4
    julia_pens = 3 * robert_pens
    dorothy_pens = julia_pens / 2

    # Calculate the total number of pens bought
    total_pens = robert_pens + julia_pens + dorothy_pens

    # Calculate the total cost of the pens
    total_cost = total_pens * cost_per_pen

    result = total_cost
    return result

print(solution())