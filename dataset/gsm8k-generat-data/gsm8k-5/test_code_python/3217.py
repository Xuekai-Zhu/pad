def solution():
    robert_pens = 4  # Robert bought 4 pens
    julia_pens = 3 * robert_pens  # Julia bought three times as many pens as Robert
    dorothy_pens = 0.5 * julia_pens  # Dorothy bought half as many pens as Julia

    total_pens = robert_pens + julia_pens + dorothy_pens  # Total number of pens bought
    cost_per_pen = 1.50  # Cost per pen is $1.50

    total_cost = total_pens * cost_per_pen  # Total cost of all pens
    result = total_cost
    return result

print(solution())