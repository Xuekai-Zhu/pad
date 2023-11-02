def solution():
    
    original_sandwiches = 20
    co_worker_sandwiches = 4
    michelle_sandwiches = 2 * co_worker_sandwiches
    remaining_sandwiches = original_sandwiches - co_worker_sandwiches - michelle_sandwiches
    result = remaining_sandwiches
    return result

print(solution())