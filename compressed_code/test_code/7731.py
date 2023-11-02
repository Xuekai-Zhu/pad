def solution():
    
    initial_number = 80000
    fourth_number = initial_number / 4
    daily_loss = 1200
    days_to_reach_fourth = (initial_number - fourth_number) / daily_loss
    result = days_to_reach_fourth
    return result

print(solution())