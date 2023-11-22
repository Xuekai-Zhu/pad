def solution():
    
    monthly_income = 2000
    shoe_price = 1000
    shoe_discount = 0.25
    shoe_income = monthly_income * shoe_discount
    shoe_price_per_pair = shoe_price
    shoe_price_per_year = shoe_income / shoe_price_per_pair * 12
    result = shoe_price_per_year
    return result

print(solution())