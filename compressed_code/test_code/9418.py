def solution():
    
    ounces_sold = 8
    price_per_ounce = 9
    earnings = ounces_sold * price_per_ounce
    fine = 50
    left_with = earnings - fine
    result = left_with
    return result

print(solution())