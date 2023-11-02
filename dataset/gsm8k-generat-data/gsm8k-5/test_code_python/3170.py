def solution():
    first_lock_time = 5  # The first lock stalls the raccoons for 5 minutes
    second_lock_time = (3 * first_lock_time) - 3  # The second lock stalls them for 3 minutes less than three times as long as the first lock
    combined_lock_time = 5 * second_lock_time  # When Karen tries both locks at once, it stalls the raccoons for five times as long as the second lock alone

    # Calculate the total time the locks stall the raccoons for
    total_time = first_lock_time + second_lock_time + combined_lock_time
    result = total_time
    return result

print(solution())