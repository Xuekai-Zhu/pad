def solution():
    original_flock_size = 100
    annual_change = 20 - 30  # Every year, the duck population changes by a net of -10
    combined_flock_size = original_flock_size  # Start with the original flock size

    # Calculate the size of the original flock after 5 years
    for year in range(5):
        combined_flock_size += annual_change  # Adjust the size of the flock based on the annual change

    # Add the second flock to the combined total
    combined_flock_size += 150

    result = combined_flock_size
    return result

print(solution())