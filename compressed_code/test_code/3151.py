def solution():
    
    taco_salad_cost = 10
    hamburgers_cost = 5 * 5
    french_fries_cost = 4 * 2.5
    peach_lemonade_cost = 5 * 2
    total_cost = taco_salad_cost + hamburgers_cost + french_fries_cost + peach_lemonade_cost
    cost_per_person = total_cost / 5
    result = cost_per_person
    return result

print(solution())