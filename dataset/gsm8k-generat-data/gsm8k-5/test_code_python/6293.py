def solution():
    initial_investment = 1000
    interest_rate = 0.1
    years = 3

    # Calculate the total amount of interest earned
    total_interest = initial_investment * interest_rate * years

    # Calculate the final amount of money John has
    final_amount = initial_investment + total_interest
    result = final_amount
    return result

print(solution())