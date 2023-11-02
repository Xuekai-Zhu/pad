def solution():
    """Jason is trying to figure out whether he can afford a new car. The car he wants costs $32,000, and he can make a down payment of $8,000. He'll have to get a loan for the rest of the amount and make 48 equal monthly payments on it. Each month, he also has to pay interest equal to 5% of that month's payment. How much will Jason's monthly payments be?"""
    car_cost = 32000
    down_payment = 8000
    loan_amount = car_cost - down_payment
    num_payments = 48
    interest_rate = 0.05
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**-num_payments)
    result = monthly_payment
    return result

print(solution())