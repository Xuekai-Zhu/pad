def solution():
    # Define the initial amount of money Janet has saved
    initial_savings = 2225

    # Define the cost of one month's rent
    monthly_rent = 1250

    # Calculate the amount of money needed for 2 months' rent in advance
    advance_rent = 2 * monthly_rent

    # Calculate the total amount of money needed for the deposit and 2 months' rent in advance
    total_cost = advance_rent + 500

    # Calculate the amount of money Janet still needs to rent the apartment
    remaining_cost = total_cost - initial_savings

    result = remaining_cost
    return result

print(solution())