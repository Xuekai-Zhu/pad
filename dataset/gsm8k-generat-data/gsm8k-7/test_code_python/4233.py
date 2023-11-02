def solution():
    num_people = 40
    potatoes_per_person = 1.5
    potatoes_needed = num_people * potatoes_per_person

    cost_per_bag = 5
    weight_per_bag = 20
    bags_needed = potatoes_needed / weight_per_bag

    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())