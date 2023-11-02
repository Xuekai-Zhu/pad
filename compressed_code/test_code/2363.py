def solution():
    
    total_miles = 493
    first_day_miles = 125
    second_day_miles = 223
    third_day_miles = total_miles - first_day_miles - second_day_miles
    result = third_day_miles
    return result

print(solution())