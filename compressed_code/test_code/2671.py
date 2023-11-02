def solution():
    
    first_day_earnings = 10
    total_earnings = first_day_earnings
    for i in range(2, 6):
        day_earnings = first_day_earnings + (i-1) * 4
        total_earnings += day_earnings
    result = total_earnings
    return result

print(solution())