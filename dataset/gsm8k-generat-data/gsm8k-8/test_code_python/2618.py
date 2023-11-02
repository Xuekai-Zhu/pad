def solution():
    # Define the number of sandwiches given to one co-worker
    coworker_sandwiches = 4

    # Calculate the number of sandwiches Michelle kept for herself
    michelle_sandwiches = coworker_sandwiches * 2

    # Calculate the total number of sandwiches used
    total_sandwiches = michelle_sandwiches + coworker_sandwiches

    # Calculate the number of sandwiches left to give to other co-workers
    sandwiches_left = 20 - total_sandwiches
    result = sandwiches_left
    return result

print(solution())