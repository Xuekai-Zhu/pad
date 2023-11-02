def solution():
    # Define the cost of the DVD for Mike
    mike_cost = 5

    # Define the cost of the DVD for Steve
    steve_cost = 2 * mike_cost

    # Define the shipping cost as a percentage of the DVD cost
    shipping_percentage = 0.8

    # Calculate the shipping cost for Steve
    shipping_cost = shipping_percentage * steve_cost

    # Calculate the total cost for Steve, including the DVD cost and shipping cost
    total_cost = steve_cost + shipping_cost
    result = total_cost
    return result

print(solution())