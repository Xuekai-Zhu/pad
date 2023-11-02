def solution():
    op_expenses = 100
    total_payments = op_expenses * (3/4)

    # Calculate the loss by subtracting the total payments received from the operations expenses
    loss = op_expenses - total_payments
    result = loss
    return result

print(solution())