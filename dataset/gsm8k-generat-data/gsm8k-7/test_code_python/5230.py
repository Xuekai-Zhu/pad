def solution():
    initial_amount = 90
    interest_rate = 0.1  # 10% interest rate
    num_years = 1

    # Calculate the amount of money Tara will have after one year with interest
    total_amount = initial_amount * (1 + interest_rate) ** num_years
    result = total_amount
    return result

print(solution())