def solution():
    # Define the number of cans and the space they take up before and after being compacted
    num_cans = 60
    pre_compacted_space = 30 * num_cans
    post_compacted_space = pre_compacted_space * 0.2

    result = post_compacted_space
    return result

print(solution())