def solution():
    
    first_lock_time = 5
    second_lock_time = (3 * first_lock_time) - 3
    time_with_both_locks = 5 * second_lock_time
    result = time_with_both_locks
    return result

print(solution())