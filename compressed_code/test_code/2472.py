def solution():
    
    bread_calories = 100
    peanut_butter_calories = 200
    total_calories = 500
    bread_count = 1
    peanut_butter_count = (total_calories - (bread_calories * bread_count)) / peanut_butter_calories
    result = peanut_butter_count
    return result

print(solution())