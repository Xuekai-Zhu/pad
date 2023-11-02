def solution():
    principal = 1000
    rate = 0.1  # 10% interest rate
    time = 3  # 3 years

    # Calculate the total interest
    interest = principal * rate * time

    # Calculate the total amount of money John has after 3 years
    total_money = principal + interest
    result = total_money
    return result

print(solution())