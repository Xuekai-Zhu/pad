def solution():
    # Define initial amount and interest rate
    initial_amount = 100
    interest_rate = 0.1

    # Calculate final amount after 1 year
    first_year_amount = initial_amount + (initial_amount * interest_rate)

    # Calculate final amount after 2 years
    final_amount = first_year_amount + (first_year_amount * interest_rate)

    result = final_amount
    return result

print(solution())