def solution():
    
    first_day = 50
    second_day = first_day * 2
    third_day = second_day + 20
    total_first_three_days = first_day + second_day + third_day
    fourth_day = total_first_three_days * 2
    total_eggs = first_day + second_day + third_day + fourth_day
    result = total_eggs
    return result

print(solution())