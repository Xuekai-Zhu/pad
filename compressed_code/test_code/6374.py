def solution():
    
    total_budget = 60
    cost_of_hummus = 5 * 2
    cost_of_chicken = 20
    cost_of_bacon = 10
    cost_of_vegetables = 10
    total_spent = cost_of_hummus + cost_of_chicken + cost_of_bacon + cost_of_vegetables
    remaining_budget = total_budget - total_spent
    apples_cost = 2
    no_of_apples = remaining_budget // apples_cost
    result = no_of_apples

    return result

print(solution())