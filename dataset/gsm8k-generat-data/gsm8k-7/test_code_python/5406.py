def solution():
    num_adults = 2  # Mr. and Mrs. Boyden
    num_children = 3

    total_cost = 77

    # Let the cost of a child ticket be x.
    # Then the cost of an adult ticket is x + 6.

    # Write an equation relating the number of tickets and the total cost
    # (number of adults) * (cost of adult ticket) + (number of children) * (cost of child ticket) = total cost

    # Simplifying the above equation, we get
    # 2(x + 6) + 3x = 77
    # 2x + 12 + 3x = 77
    # 5x = 65
    # x = 13

    # Therefore, the cost of an adult ticket is x + 6 = $19.
    adult_ticket_cost = 19
    result = adult_ticket_cost
    return result

print(solution())