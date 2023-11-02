def solution():
    down_payment = 5000
    monthly_payment = 250
    number_of_payments = 60
    total_payment = monthly_payment * number_of_payments
    price_of_car = total_payment + down_payment
    result = price_of_car
    
    return result

print(solution())