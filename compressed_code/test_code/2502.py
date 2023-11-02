def solution():
    
    robert_pens = 4
    julia_pens = 3 * robert_pens
    dorothy_pens = 0.5 * julia_pens
    total_pens = robert_pens + julia_pens + dorothy_pens
    pen_price = 1.5
    total_cost = total_pens * pen_price
    result = total_cost
    return result

print(solution())