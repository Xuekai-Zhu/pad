def solution():
    max_crate_weight = 20
    num_crates = 15
    num_nail_bags = 4
    weight_nail_bags = 5
    num_hammer_bags = 12
    weight_hammer_bags = 5
    num_plank_bags = 10
    weight_plank_bags = 30
    
    total_weight = (num_nail_bags * weight_nail_bags) + (num_hammer_bags * weight_hammer_bags) + (num_plank_bags * weight_plank_bags)
    weight_over_limit = total_weight - (max_crate_weight * num_crates)
    result = weight_over_limit
    
    return result

print(solution())