def solution():
    """Tamara is 3 times Kim's height less 4 inches. Tamara and Kim have a combined height of 92 inches. How many inches tall is Tamara?"""
    combined_height = 92
    t_to_k_ratio = 3
    t_to_k_difference = 4
    k_height = (combined_height - t_to_k_difference) / (t_to_k_ratio + 1)
    t_height = k_height * t_to_k_ratio + t_to_k_difference
    result = t_height
    return result

print(solution())