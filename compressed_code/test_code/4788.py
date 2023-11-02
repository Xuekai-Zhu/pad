def solution():
    
    refrigerators_per_hour = 90
    coolers_per_hour = refrigerators_per_hour + 70
    hours_per_day = 9
    products_per_day = (refrigerators_per_hour + coolers_per_hour) * hours_per_day
    products_per_5_days = products_per_day * 5

    result = products_per_5_days
    return result

print(solution())