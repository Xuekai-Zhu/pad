def solution():
    # Calculate the total cost of the two transactions with the service charge
    total_cost = (90 * 1.02) + (60 * 1.02)

    # Subtract the total cost from the account balance before the transactions
    new_balance = 400 - total_cost

    # Add the reversed transaction back to the account balance
    new_balance += 60

    result = new_balance
    return result

print(solution())