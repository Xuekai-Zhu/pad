def solution():
    
    num_of_classes = 5
    num_of_boards_per_class = 2
    ink_per_board_per_day = 20
    ink_cost_per_ml = 0.5
    total_ink_needed = num_of_classes * num_of_boards_per_class * ink_per_board_per_day
    total_cost = total_ink_needed * ink_cost_per_ml
    result = total_cost
    return result

print(solution())