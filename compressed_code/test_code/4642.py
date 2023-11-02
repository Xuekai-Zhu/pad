def solution():
    
    sunday_temp = 99.1
    monday_temp = 98.2
    tuesday_temp = 98.7
    wednesday_temp = 99.3
    thursday_temp = 99.8
    friday_temp = 99
    saturday_temp = 98.9

    total_temp = sunday_temp + monday_temp + tuesday_temp + wednesday_temp + thursday_temp + friday_temp + saturday_temp
    average_temp = total_temp / 7
    result = average_temp
    return result

print(solution())