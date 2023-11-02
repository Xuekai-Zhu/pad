def solution():
    total_chars = 60

    # Calculate the number of characters with initial A
    num_a_chars = total_chars // 2

    # Calculate the number of characters with initial C
    num_c_chars = num_a_chars // 2

    # Calculate the number of characters with initial D
    num_d_chars = (total_chars - num_a_chars - num_c_chars) // 3 * 2

    result = num_d_chars
    return result

print(solution())