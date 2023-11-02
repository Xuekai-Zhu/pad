def solution():
    
    weekday_rate = 420
    weekend_rate = 540
    rental_days = 4
    total_weekday_rental = weekday_rate * 2  
    total_weekend_rental = weekend_rate * 2  
    total_rental_cost = total_weekday_rental + total_weekend_rental
    cost_per_person = total_rental_cost / 6  
    result = cost_per_person
    return result

print(solution())