def solution():
    
    previous_tree_height = 6
    previous_rung_count = 12
    current_tree_height = 20
    current_rung_count = (previous_rung_count/previous_tree_height)*current_tree_height
    result = current_rung_count
    return result

print(solution())