def solution():
    total_cost = 110  # The total cost of the items was $110
    james_coat = 40  # Mary bought James a coat for $40
    jamie_shoes = 30  # Mary bought Jamie a pair of shoes for $30

    # Calculate the total cost of the two pairs of jeans for James
    jeans_cost = total_cost - james_coat - jamie_shoes
    # Divide the cost of the two pairs of jeans by 2 to get the cost of one pair of jeans
    cost_per_jeans = jeans_cost / 2
    result = cost_per_jeans
    return result

print(solution())