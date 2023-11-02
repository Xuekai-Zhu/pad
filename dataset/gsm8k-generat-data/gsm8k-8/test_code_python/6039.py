def solution():
    # Define the total operation cost and total revenue from clients
    operation_cost = 100
    client_revenue = 0.75 * operation_cost

    # Calculate the loss the hotel incurred
    loss = operation_cost - client_revenue
    result = loss
    return result

print(solution())