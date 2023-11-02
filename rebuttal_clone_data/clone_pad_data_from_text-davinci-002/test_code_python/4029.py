def solution():
    pops_sold = 100
    cost_to_make_pop = 0.90
    money_made = pops_sold * 1.50
    cost_of_goods = 100 * 1.80
    result = cost_of_goods / (money_made - cost_to_make_pop)
    return result

print(solution())