def solution():
    sandwiches_to_one = 4  # Michelle gives 4 sandwiches to one co-worker
    sandwiches_kept = 2 * sandwiches_to_one  # Michelle keeps twice as many sandwiches as she gives to one co-worker
    total_sandwiches = 20  # Michelle originally made 20 sandwiches

    # Calculate how many sandwiches Michelle has left to give to other co-workers
    left_to_give = total_sandwiches - sandwiches_to_one - sandwiches_kept
    result = left_to_give
    return result

print(solution())