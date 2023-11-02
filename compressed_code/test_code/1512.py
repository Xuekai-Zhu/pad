def solution():
    
    initial_chips_eaten = 10
    remaining_chips = 100 - initial_chips_eaten
    days_to_finish_remaining_chips = remaining_chips / 10
    total_days = 1 + days_to_finish_remaining_chips
    result = total_days
    return result

print(solution())