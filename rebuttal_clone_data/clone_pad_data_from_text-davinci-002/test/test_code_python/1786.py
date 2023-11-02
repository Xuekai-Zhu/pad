def solution():
    cost_laptop = 600
    cost_smartphone = 400
    quantity_laptop = 2
    quantity_smartphone = 4
    total_cost = quantity_laptop * cost_laptop + quantity_smartphone * cost_smartphone
    money_given = 3000
    change = money_given - total_cost
    result = change
    return result

print(solution())