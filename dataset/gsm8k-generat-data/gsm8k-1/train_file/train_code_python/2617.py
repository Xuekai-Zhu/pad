def solution():
    """Michelle is bringing sandwiches to work to give to her co-workers. She gives 4 sandwiches to one of her co-workers and keeps twice this amount for herself. If she had originally made 20 sandwiches, how many sandwiches does she have left to give to her other co-workers?"""
    original_sandwiches = 20
    co_worker_sandwiches = 4
    michelle_sandwiches = 2 * co_worker_sandwiches
    remaining_sandwiches = original_sandwiches - co_worker_sandwiches - michelle_sandwiches
    result = remaining_sandwiches
    return result

print(solution())