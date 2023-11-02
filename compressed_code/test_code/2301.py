def solution():
    
    gas_cost = 17 * 3
    rides_given = 3
    hours_worked = 8
    hourly_wage = 15
    ride_bonus = 5
    review_bonus = 20
    total_wage = (hours_worked * hourly_wage) + (rides_given * ride_bonus) + (2 * review_bonus) + gas_cost
    result = total_wage
    return result

print(solution())