def solution():
    # Define the number of large and small tubs
    num_large = 3
    num_small = 6

    # Define the total cost of the tubs
    total_cost = 48

    # Define the cost of one large tub
    large_cost = 6

    # Calculate the cost of all the large tubs
    total_large_cost = num_large * large_cost

    # Calculate the cost of all the small tubs
    total_small_cost = total_cost - total_large_cost

    # Calculate the cost of one small tub
    small_cost = total_small_cost / num_small

    result = small_cost
    return result

print(solution())