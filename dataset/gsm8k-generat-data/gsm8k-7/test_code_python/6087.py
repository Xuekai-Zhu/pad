def solution():
    initial_amount = 100
    interest_rate = 0.1 # 10% interest rate
    num_years = 2

    # Calculate amount after interest for first year
    first_year_amount = initial_amount * (1 + interest_rate)

    # Calculate final amount after second year
    final_amount = first_year_amount * (1 + interest_rate)

    result = final_amount
    return result

print(solution())