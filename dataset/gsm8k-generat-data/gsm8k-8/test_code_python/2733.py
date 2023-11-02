def solution():
    # Calculate the size of the original flock after 5 years
    original_flock_size = 100
    for i in range(5):
        original_flock_size = original_flock_size - 20 + 30

    # Calculate the size of the combined flock
    combined_flock_size = original_flock_size + 150
    result = combined_flock_size
    return result

print(solution())