def solution():
    
    total_apples = 200
    first_day_picked = total_apples / 5
    second_day_picked = first_day_picked * 2
    third_day_picked = first_day_picked + 20
    remaining_apples = total_apples - first_day_picked - second_day_picked - third_day_picked
    result = remaining_apples
    return result

print(solution())