def solution():
    
    first_day = 50
    second_day = 2 * first_day
    third_day = second_day + 20
    total_first_three_days = first_day + second_day + third_day
    fourth_day = 2 * total_first_three_days
    total_eggs = first_day + second_day + third_day + fourth_day
    result = total_eggs
    return result

print(solution())