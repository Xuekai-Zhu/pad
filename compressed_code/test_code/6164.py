def solution():
    
    num_people = 6
    num_bags_per_person = 5
    weight_per_bag = 50
    total_weight = num_people * num_bags_per_person * weight_per_bag
    max_weight = 6000
    remaining_weight = max_weight - total_weight
    bags_remaining = remaining_weight // weight_per_bag
    result = bags_remaining
    
    return result

print(solution())