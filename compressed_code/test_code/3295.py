def solution():
    
    pounds_per_person = 1.5
    total_people = 40
    total_potatoes = pounds_per_person * total_people
    pounds_per_bag = 20
    cost_per_bag = 5
    total_bags = total_potatoes / pounds_per_bag
    total_cost = total_bags * cost_per_bag
    result = total_cost
    return result

print(solution())