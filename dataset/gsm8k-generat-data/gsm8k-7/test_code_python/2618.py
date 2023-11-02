def solution():
    num_sandwiches = 20
    coworker_sandwiches = 4

    # Calculate the amount of sandwiches Michelle keeps for herself
    michelle_sandwiches = coworker_sandwiches * 2

    # Remove the sandwiches Michelle keeps from the total
    remaining_sandwiches = num_sandwiches - michelle_sandwiches

    # Remove the sandwiches for the first co-worker
    remaining_sandwiches -= coworker_sandwiches

    result = remaining_sandwiches
    return result

print(solution())