def solution():
    """A hotel had operations expenses totaling $100. If the hotel received clients whose total payments for services offered totaled 3/4 of the cost of the operations, calculate the loss the hotel incurred."""
    operations_expenses = 100
    total_payments = operations_expenses * 3/4
    loss = operations_expenses - total_payments
    result = loss
    return result

print(solution())