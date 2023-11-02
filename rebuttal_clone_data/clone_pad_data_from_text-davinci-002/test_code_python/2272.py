def solution():
    first_week = 200
    second_week = first_week - 150
    third_week = second_week - 150
    fourth_week = third_week * 2
    total_employees = first_week + second_week + third_week + fourth_week
    average_employees = total_employees / 4
    result = average_employees
    
    return result

print(solution())