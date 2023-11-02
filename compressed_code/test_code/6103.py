def solution():
    
    starting_amount = 10000 
    morning_cooked = 9000
    remaining_after_morning = starting_amount - morning_cooked
    evening_cooked = remaining_after_morning / 4
    remaining_after_evening = remaining_after_morning - evening_cooked
    result = remaining_after_evening
    return result

print(solution())