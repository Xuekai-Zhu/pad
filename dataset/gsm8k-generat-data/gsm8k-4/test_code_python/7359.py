def solution():
    """To get ready for the new school year, Mary brought her two kids shopping. She bought her son James, a coat for $40 and two pairs of jeans. She bought his sister Jamie, a pair of shoes for $30. The total cost of the items was $110. If the two pairs of jeans for James cost the same price, how much did one pair of jeans cost?"""
    # Define the cost of the coat, shoes, and total cost
    coat_cost = 40
    shoes_cost = 30
    total_cost = 110

    # Calculate the cost of the two pairs of jeans
    jeans_cost = total_cost - coat_cost - shoes_cost

    # Calculate the cost of one pair of jeans
    one_jeans_cost = jeans_cost / 2

    # return the result
    result = one_jeans_cost
    return result

print(solution())