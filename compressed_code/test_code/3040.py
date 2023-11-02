def solution():
    
    down_payment = 5000
    monthly_payment = 250
    total_payments = 5 * 12
    remaining_balance = total_payments * monthly_payment
    car_price = remaining_balance + down_payment
    result = car_price
    return result

print(solution())