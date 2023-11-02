def solution():
    taco_salad = 10
    daves_single = 5
    french_fries = 2.50
    peach_lemonade = 2
    total_cost = taco_salad + (daves_single * 5) + (french_fries * 4) + (peach_lemonade * 5)
    cost_per_person = total_cost / 5
    result = cost_per_person
    return result

print(solution())