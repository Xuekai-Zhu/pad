def solution():
    # Calculate the total cost of dropping off the clothes
    total_cost = 140

    # Calculate the cost of the trousers
    trouser_cost = 9 * 10

    # Calculate the cost of the shirts, using the remaining total from the trouser cost
    shirt_cost = total_cost - trouser_cost

    # Calculate the number of shirts dropped off
    shirts_dropped_off = shirt_cost / 5

    # Calculate the number of shirts missing
    shirts_missing = 10 - shirts_dropped_off

    result = shirts_missing
    return result

print(solution())