def solution():
    
    daily_rate = 125
    pet_fee = 100
    service_fee_percent = 20
    rental_days = 14
    rental_cost = (daily_rate * rental_days) + pet_fee
    service_fee = rental_cost * (service_fee_percent / 100)
    total_cost = rental_cost + service_fee
    security_deposit = total_cost * 0.5
    result = security_deposit
    
    return result

print(solution())