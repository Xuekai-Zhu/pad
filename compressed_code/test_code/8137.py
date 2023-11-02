def solution():
    
    
    gas_cost = 17 * 3
    hours_worked = 8
    hourly_wage = 15
    ride_bonus = 5
    good_review_bonus = 20
    rides_given = 3
    good_reviews = 2
    
    total_earnings = (hours_worked * hourly_wage) + (rides_given * ride_bonus) + (good_reviews * good_review_bonus) + gas_cost
    
    result = total_earnings
    
    return result

print(solution())