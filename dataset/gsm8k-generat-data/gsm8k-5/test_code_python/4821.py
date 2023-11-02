def solution():
    monthly_cost = 12  # The gym costs $12 per month
    down_payment = 50  # There is a $50 down payment

    # Calculate the total cost for 3 years, including the down payment
    total_cost = down_payment + (monthly_cost * 12 * 3)

    result = total_cost
    return result

print(solution())