def solution():
    
    kids_price = 3
    adults_price = 2 * kids_price
    kids_count = 8
    adults_count = 10
    daily_earnings = kids_count * kids_price + adults_count * adults_price
    weekly_earnings = daily_earnings * 7
    result = weekly_earnings
    return result

print(solution())