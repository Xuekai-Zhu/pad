def solution():
    
    car_price = 35000
    loan_amount = 20000
    loan_interest_rate = 0.15
    loan_interest = loan_amount * loan_interest_rate
    total_price = car_price + loan_interest
    result = total_price
    return result

print(solution())