def solution():
    initial_investment = 300
    monthly_interest_rate = 0.1
    num_months = 2

    # Calculate the total amount of interest earned
    total_interest = initial_investment * monthly_interest_rate * num_months

    # Calculate the total amount of money at the end of 2 months, including interest
    total_amount = initial_investment + total_interest
    result = total_amount
    return result

print(solution())