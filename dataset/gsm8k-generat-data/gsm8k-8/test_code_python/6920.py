def solution():
    # Define the initial deposit and interest rate
    initial_deposit = 5600
    interest_rate = 0.07

    # Calculate the total amount after the first year
    year1_amount = initial_deposit + (initial_deposit * interest_rate)

    # Calculate the total amount after the second year
    year2_amount = year1_amount + (year1_amount * interest_rate)

    result = year2_amount
    return result

print(solution())