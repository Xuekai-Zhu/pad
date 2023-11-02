def solution():
    original_capacity = 3000 # in 8MB each
    original_size = 8 # in MB each
    new_size = 6 # in MB each

    # Calculate the new capacity
    new_capacity = (original_capacity * original_size) / new_size
    result = int(new_capacity)
    return result

print(solution())