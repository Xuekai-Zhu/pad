def solution():
    # Calculate the total amount of money after 2.5 years with 8% interest
    deposit = 2000  # amount deposited
    interest_rate = 0.08  # 8% interest rate
    time = 2.5  # 2 and a half years
    interest = deposit * interest_rate * time  # interest earned
    total_amount = deposit + interest  # total amount of money
    result = round(total_amount, 2)
    return result

print(solution())