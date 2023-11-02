def solution():
    
    kids_price = 3
    adults_price = 2 * kids_price
    kids_per_day = 8
    adults_per_day = 10
    total_kids_price = kids_price * kids_per_day * 7
    total_adults_price = adults_price * adults_per_day * 7
    total_income_per_week = total_kids_price + total_adults_price
    result = total_income_per_week
    return result

print(solution())