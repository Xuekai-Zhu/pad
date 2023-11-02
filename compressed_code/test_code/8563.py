def solution():
    
    total_goal = 1000
    months_to_save = 12
    starting_amount = 100
    amount_left_to_save = total_goal - starting_amount
    amount_to_save_per_month = amount_left_to_save / months_to_save
    result = amount_to_save_per_month
    return result

print(solution())