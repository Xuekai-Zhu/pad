def solution():
    # Calculate the total amount of money spent and the remaining balance
    total_spent = 2.75 + 1.50 + 11.50  # the total amount spent
    remaining_balance = 40 - total_spent  # the remaining balance

    # Calculate the number of quarters Phil has left
    quarters = int(remaining_balance / 0.25)
    result = quarters
    return result

print(solution())