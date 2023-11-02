def solution():
    """Michelle is bringing sandwiches to work to give to her co-workers. She gives 4 sandwiches to one of her co-workers and keeps twice this amount for herself. If she had originally made 20 sandwiches, how many sandwiches does she have left to give to her other co-workers?"""
    # Define the number of sandwiches Michelle made
    total_sandwiches = 20

    # Calculate the number of sandwiches Michelle gave to her co-worker
    coworker_sandwiches = 4

    # Calculate the number of sandwiches Michelle kept for herself
    michelle_sandwiches = coworker_sandwiches * 2

    # Calculate the number of sandwiches Michelle has left to give to her other co-workers
    leftover_sandwiches = total_sandwiches - coworker_sandwiches - michelle_sandwiches

    # Return the result
    result = leftover_sandwiches
    return result

print(solution())