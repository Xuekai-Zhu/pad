def solution():
    house_price = 280000
    deposit = 40000
    mortgage_amount = house_price - deposit
    mortgage_term = 10
    monthly_payment = mortgage_amount / (mortgage_term * 12)
    result = monthly_payment
    return result

print(solution())