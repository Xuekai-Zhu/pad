def solution():
    robert_pens = 4
    julia_pens = 3 * robert_pens
    dorothy_pens = julia_pens / 2
    pen_price = 1.5

    # Calculate the total number of pens bought
    total_pens = robert_pens + julia_pens + dorothy_pens

    # Calculate the total cost of all pens bought
    total_cost = total_pens * pen_price
    result = total_cost
    return result

print(solution())