def solution():
    
    starting_shells = 20
    shells_per_day = 5
    vacation_days = 3
    additional_shells = shells_per_day * vacation_days
    fourth_day_shells = 6
    total_shells = starting_shells + additional_shells + fourth_day_shells
    result = total_shells
    return result

print(solution())