def solution():
    # Calculate the number of cheerleaders who need a size 6
    num_size_2 = 4
    num_size_12 = 0.5 * num_size_6  # half the number of size 6 cheerleaders need a size 12
    total_cheerleaders = 19
    num_size_6 = total_cheerleaders - num_size_2 - num_size_12  # total number of size 6 cheerleaders

    result = num_size_6
    return result

print(solution())