def solution():
    people = 6
    bags_per_person = 5
    max_weight_per_bag = 50
    total_weight = people * bags_per_person * max_weight_per_bag
    max_weight_allowed = 6000
    remaining_weight = max_weight_allowed - total_weight
    bags_allowed = remaining_weight / max_weight_per_bag
    result = bags_allowed
    return result

print(solution())