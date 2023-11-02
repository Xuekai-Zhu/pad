def solution():
    # Determine the total amount of the allowance
    total_allowance = 100

    # Calculate the amount Mitzel spent as a decimal
    percent_spent = 35/100
    amount_spent = percent_spent * total_allowance

    # Calculate the amount of money left in the allowance
    amount_left = total_allowance - amount_spent - 14
    result = amount_left
    return result

print(solution())