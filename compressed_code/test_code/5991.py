def solution():
    
    saturday_earnings = 18
    sunday_earnings = saturday_earnings / 2
    previous_weekend_earnings = 20
    total_earnings = saturday_earnings + sunday_earnings + previous_weekend_earnings
    needed_earnings = 60 - total_earnings
    result = needed_earnings
    return result

print(solution())