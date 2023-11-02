def solution():
    
    daily_average = 40
    friday_increase = 0.4
    friday_borrowed = daily_average * (1 + friday_increase)
    total_borrowed = daily_average * 4 + friday_borrowed
    result = total_borrowed
    return result

print(solution())