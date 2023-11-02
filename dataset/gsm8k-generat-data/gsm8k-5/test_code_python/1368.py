def solution():
    total_height = 92  # Tamara and Kim have a combined height of 92 inches
    t_to_k_ratio = 3  # Tamara's height is 3 times Kim's height
    t_minus_k = 4  # Tamara's height is 3 times Kim's height less 4 inches

    # Calculate Kim's height
    k_height = (total_height - t_minus_k) / (t_to_k_ratio + 1)

    # Calculate Tamara's height
    t_height = t_to_k_ratio * k_height + t_minus_k
    result = t_height
    return result

print(solution())