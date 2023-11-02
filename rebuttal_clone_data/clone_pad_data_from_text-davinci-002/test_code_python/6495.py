def solution():
    pieces_of_firewood_per_tree = 75
    logs_needed_per_day = 5
    days_in_period = 89
    total_pieces_of_firewood_needed = logs_needed_per_day * days_in_period
    total_trees_needed = total_pieces_of_firewood_needed / pieces_of_firewood_per_tree
    result = total_trees_needed
    
    return result

print(solution())