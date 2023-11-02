def solution():
    
    daily_rental_price = 50
    two_week_rental_price = 500
    days_in_two_weeks = 14
    additional_days = 20 - days_in_two_weeks
    
    if additional_days <= 0:
        total_cost = two_week_rental_price
    else:
        additional_cost = additional_days * daily_rental_price
        total_cost = two_week_rental_price + additional_cost
    
    result = total_cost
    return result

print(solution())