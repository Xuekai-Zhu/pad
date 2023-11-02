def solution():
    apple_weight = 4  # ounce
    orange_weight = 3  # ounce
    max_weight_per_bag = 49  # ounce
    num_bags = 3
    
    total_fruit_weight = max_weight_per_bag * num_bags
    num_fruits_per_bag = max_weight_per_bag // (apple_weight + orange_weight)
    num_apples_per_bag = num_fruits_per_bag // 2  # equal number of apples and oranges
    total_num_apples = num_apples_per_bag * num_bags
    total_apple_weight = total_num_apples * apple_weight
    
    result = total_apple_weight
    return result

print(solution())