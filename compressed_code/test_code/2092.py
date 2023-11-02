def solution():
    
    daily_rate = 125.00
    pet_fee = 100.00
    rental_duration = 14
    sub_total = (daily_rate * rental_duration) + pet_fee
    service_fee = 0.2 * sub_total
    total_bill = sub_total + service_fee
    security_deposit = 0.5 * total_bill
    result = security_deposit
    return result

print(solution())