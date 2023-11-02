def solution():
    
    people = 15
    pounds_per_person = 2
    total_pounds = people * pounds_per_person
    bags_needed = total_pounds / 10
    cost_per_bag = 3
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())