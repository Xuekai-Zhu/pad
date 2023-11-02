def solution():
    
    postcards_per_day = 30
    selling_price = 5
    days = 6
    total_postcards = postcards_per_day * days
    total_earnings = total_postcards * selling_price
    result = total_earnings
    return result

print(solution())