def solution():
    num_sticky_keys = 15 # Tina counts 15 keys that are sticky
    time_per_key = 3 # It takes Tina 3 minutes to clean one key
    time_remaining = 10 # Tina's assignment will take her 10 minutes to complete
    time_to_clean_all_keys = num_sticky_keys * time_per_key # Multiplying time_per_key by num_sticky_keys to determine total cleaning time
    total_time = time_remaining + time_to_clean_all_keys # Adding the time required to complete the assignment to the time required to clean all keys
    result = total_time
    return result

print(solution())