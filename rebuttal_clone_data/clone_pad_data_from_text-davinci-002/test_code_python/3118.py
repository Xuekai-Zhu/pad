def solution():
    car_cost = 32000
    down_payment = 8000
    loan_amount = car_cost - down_payment
    monthly_interest_rate = 0.05
    monthly_payment = loan_amount / 48 + (loan_amount * monthly_interest_rate)
    result = monthly_payment
    return result

print(solution())