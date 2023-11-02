def solution():
    num_size_2 = 4
    num_size_6 = None   # We need to find this value
    num_size_12 = None  # We will find this using num_size_6
    total_cheerleaders = 19

    # Calculate the number of cheerleaders who need size 12 uniforms
    num_size_12 = total_cheerleaders - num_size_2 - num_size_6

    # Use the fact that half the number of size 6 uniforms is equal to the number of size 12 uniforms
    num_size_6 = num_size_12 * 2

    result = num_size_6
    return result

print(solution())