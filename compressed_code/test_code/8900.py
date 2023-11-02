def solution():
    
    total_people = 1 + 14
    pizzas_needed = (total_people // 3) + (total_people % 3 > 0)
    cost_per_pizza = 12
    total_cost = pizzas_needed * cost_per_pizza
    nights_babysitting = total_cost // 4
    result = nights_babysitting
    return result

print(solution())