def solution():
    """Shiela bought five cell phones for $150 each for a 3-month installment. A 2% interest will be charged for each unit. How much will Shiela pay each month for 3 months?"""
    num_phones = 5
    phone_cost = 150
    interest_rate = 0.02
    total_cost = num_phones * phone_cost * (1 + interest_rate)
    monthly_payment = total_cost / 3
    result = monthly_payment
    return result

print(solution())