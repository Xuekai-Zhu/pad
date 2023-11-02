def solution():
    # Define initial balance and first expense
    balance = 55
    shirt_expense = 7

    # Update balance after buying the shirt
    balance -= shirt_expense

    # Calculate and add second expense
    second_expense = 3 * shirt_expense
    balance -= second_expense

    result = balance
    return result

print(solution())