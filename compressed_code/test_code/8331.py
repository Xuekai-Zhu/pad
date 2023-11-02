def solution():
    
    robert_pens = 4
    julia_pens = robert_pens * 3
    dorothy_pens = julia_pens / 2
    total_pens = robert_pens + julia_pens + dorothy_pens
    pen_cost = 1.5
    total_cost = total_pens * pen_cost
    result = total_cost
    return result

print(solution())