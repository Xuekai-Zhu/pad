def solution():
    
    friday_earnings = 147
    saturday_earnings = 2 * friday_earnings + 7
    sunday_earnings = friday_earnings + 78
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())