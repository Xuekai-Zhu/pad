def solution():
    # Calculate how long it will take to clean all the keys
    time_per_key = 3  # minutes it takes to clean one key
    keys_left = 14  # number of keys left to clean
    total_key_time = time_per_key * keys_left

    # Calculate the total time needed to finish the homework and clean the keys
    homework_time = 10  # minutes needed to complete the homework
    total_time = total_key_time + homework_time

    result = total_time
    return result

print(solution())