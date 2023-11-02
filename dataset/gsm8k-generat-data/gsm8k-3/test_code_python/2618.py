def solution():
    """Michelle is bringing sandwiches to work to give to her co-workers. She gives 4 sandwiches to one of her co-workers and keeps twice this amount for herself. If she had originally made 20 sandwiches, how many sandwiches does she have left to give to her other co-workers?"""
    # Define the number of sandwiches given to one co-worker
    co_worker = 4

    # Calculate the number of sandwiches Michelle kept for herself
    michelle = co_worker * 2

    # Calculate the number of sandwiches left for the other co-workers
    left_over = 20 - co_worker - michelle

    # Display the number of sandwiches left over
    result = left_over
    return result

print(solution())