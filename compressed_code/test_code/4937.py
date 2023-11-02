def solution():
    
    
    num_cases = 13
    num_children_group1 = 14
    num_children_group2 = 16
    num_children_group3 = 12
    num_children_group4 = (num_children_group1 + num_children_group2 + num_children_group3) / 2
    num_bottles_per_child_per_day = 3
    num_days = 3
    
    num_bottles_needed = (num_children_group1 + num_children_group2 + num_children_group3 + num_children_group4) * num_bottles_per_child_per_day * num_days
    num_bottles_available = num_cases * 24
    
    num_bottles_to_buy = num_bottles_needed - num_bottles_available
    
    result = num_bottles_to_buy
    return result

print(solution())