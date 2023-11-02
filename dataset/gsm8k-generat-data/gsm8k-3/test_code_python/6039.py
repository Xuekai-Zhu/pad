def solution():
    """A hotel had operations expenses totaling $100. If the hotel received clients whose total payments for services offered totaled 3/4 of the cost of the operations, calculate the loss the hotel incurred."""
    # Define the total operations expense and the total payments from clients
    operations_expense = 100
    total_payments = 3/4 * operations_expense

    # Calculate the loss incurred by the hotel
    loss = operations_expense - total_payments

    # Display the loss incurred
    result = loss
    return result

print(solution())