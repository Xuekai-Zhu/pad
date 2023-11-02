def solution():
    # Calculate Michelle's initial number of sandwiches
    initial_sandwiches = 20

    # Calculate how many sandwiches Michelle keeps for herself
    sandwiches_kept = 4 * 2

    # Calculate the remaining number of sandwiches to give to other co-workers
    remaining_sandwiches = initial_sandwiches - 4 - sandwiches_kept
    result = remaining_sandwiches
    return result

print(solution())