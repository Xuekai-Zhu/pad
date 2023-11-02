def solution():
    """To get ready for the new school year, Mary brought her two kids shopping. She bought her son James, a coat for $40 and two pairs of jeans. She bought his sister Jamie, a pair of shoes for $30. The total cost of the items was $110. If the two pairs of jeans for James cost the same price, how much did one pair of jeans cost?"""
    # Define the cost of the coat, shoes, and total cost
    cost_coat = 40
    cost_shoes = 30
    total_cost = 110

    # Calculate the cost of the two pairs of jeans
    cost_jeans = total_cost - cost_coat - cost_shoes

    # Calculate the cost of one pair of jeans
    cost_one_jean = cost_jeans / 2

    # Display the cost of one pair of jeans
    result = cost_one_jean
    return result

print(solution())