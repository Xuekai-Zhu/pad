def solution():
    cash_price = 400
    down_payment = 120
    monthly_payment = 30
    num_months = 12

    # Calculate the total cost of paying with the down payment and monthly payments
    total_cost = down_payment + (monthly_payment * num_months)

    # Calculate the amount saved by paying cash
    savings = total_cost - cash_price
    result = savings
    return result

print(solution())