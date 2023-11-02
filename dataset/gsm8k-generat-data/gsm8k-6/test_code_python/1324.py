def solution():
    # Calculate the cost of lunch for Rick
    rick_cost = 45 * 2  # since Adam spends two-thirds as much money as Rick and we know Jose ate lunch worth $45

    # Calculate the total cost of lunch for all three friends
    total_cost = rick_cost + 45  # since Rick and Jose eat lunch of the same price

    result = total_cost
    return result

print(solution())