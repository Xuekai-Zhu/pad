def solution():
    # Calculate the total number of marbles sold to the customers
    total_sold = 20 * 15  # each customer bought 15 marbles

    # Calculate the number of marbles remaining in the store
    remaining_marbles = 400 - total_sold

    result = remaining_marbles
    return result

print(solution())