def solution():
    car_cost = 18000
    down_payment = 3000
    total_cost = car_cost + down_payment
    monthly_installments = 6
    monthly_payment = total_cost / monthly_installments
    result = monthly_payment
    return result

print(solution())