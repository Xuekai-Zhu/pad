def solution():
    first_lock = 5
    second_lock = 3 * first_lock - 3
    both_locks = 5 * second_lock

    # Calculate the total time the raccoons are stalled with both locks
    total_time = first_lock + second_lock + both_locks
    result = total_time
    return result

print(solution())