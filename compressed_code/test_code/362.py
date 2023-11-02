def solution():
    
    num_people = 6
    num_bags_per_person = 5
    bag_weight = 50
    total_luggage_weight = num_people * num_bags_per_person * bag_weight
    remaining_weight_capacity = 6000 - total_luggage_weight
    remaining_bags_capacity = remaining_weight_capacity / bag_weight
    result = remaining_bags_capacity
    return result

print(solution())