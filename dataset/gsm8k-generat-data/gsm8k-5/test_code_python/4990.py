def solution():
    # Calculate the total cost of the bill
    total_cost = 140

    # Calculate the cost of the trousers
    trouser_cost = 9 * 10  # Leo dropped off 10 pairs of trousers

    # Calculate the cost of the shirts
    shirt_cost = total_cost - trouser_cost

    # Calculate the number of shirts based on the cost
    num_shirts = shirt_cost / 5

    # Calculate the number of shirts missing
    num_missing_shirts = 10 - num_shirts

    result = num_missing_shirts
    return result

print(solution())