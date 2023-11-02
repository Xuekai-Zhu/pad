def solution():
    """Gary bought his first used car for $6,000. Gary borrowed the money from his dad who said he could pay him back the full amount over 5 years. Gary decided he would pay his dad back the full amount in 2 years. How much more is Gary spending per month to pay the loan off in 2 years instead of 5?"""
    cost_of_car = 6000
    interest_rate = 0.12
    months_in_loan_5_years = 60
    monthly_payment_5_years = cost_of_car * ((interest_rate / 12) * (1 + (interest_rate / 12)) ** months_in_loan_5_years) / (((1 + (interest_rate / 12)) ** months_in_loan_5_years) - 1)
    months_in_loan_2_years = 24
    monthly_payment_2_years = cost_of_car * ((interest_rate / 12) * (1 + (interest_rate / 12)) ** months_in_loan_2_years) / (((1 + (interest_rate / 12)) ** months_

print(solution())