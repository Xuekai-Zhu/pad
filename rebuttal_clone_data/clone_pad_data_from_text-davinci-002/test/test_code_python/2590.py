def solution():
    number_of_peach_pies = 5
    number_of_apple_pies = 4
    number_of_blueberry_pies = 3
    pounds_of_fruit_per_pie = 3
    pounds_of_peaches_needed = number_of_peach_pies * pounds_of_fruit_per_pie
    pounds_of_apples_needed = number_of_apple_pies * pounds_of_fruit_per_pie
    pounds_of_blueberries_needed = number_of_blueberry_pies * pounds_of_fruit_per_pie
    cost_of_peaches = 2.00
    cost_of_apples = 1.00
    cost_of_blueberries = 1.00
    total_cost = (pounds_of_peaches_needed * cost_of_peaches) + (pounds_of_apples_needed * cost_of_apples) + (pounds_of_blueberries_needed * cost_of_blueberries)
    result = total_cost
    return result

print(solution())