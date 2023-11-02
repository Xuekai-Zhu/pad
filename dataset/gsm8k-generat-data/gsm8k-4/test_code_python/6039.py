def solution():
    """A hotel had operations expenses totaling $100. If the hotel received clients whose total payments for services offered totaled 3/4 of the cost of the operations, calculate the loss the hotel incurred."""
    # Define the total cost of operations
    operations_cost = 100

    # Calculate the total payments for services offered
    service_payments = operations_cost * 3/4

    # Calculate the loss incurred by the hotel
    loss = operations_cost - service_payments

    # return the result
    result = loss
    return result

print(solution())