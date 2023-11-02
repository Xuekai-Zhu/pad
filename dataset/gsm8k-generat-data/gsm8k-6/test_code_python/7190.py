def solution():
    # Calculate the potential revenue if the theater had sold out
    potential_revenue = 50 * 8  # capacity of theater multiplied by ticket price

    # Calculate the actual revenue based on the number of tickets sold
    actual_revenue = 24 * 8  # number of tickets sold multiplied by ticket price

    # Calculate the loss in revenue due to not selling out
    loss = potential_revenue - actual_revenue
    result = loss
    return result

print(solution())