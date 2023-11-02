def solution():
    # Calculate the number of red apples from the first tree
    num_red_first_tree = 0.4 * 20  # 40% of 20 apples

    # Calculate the number of red apples from the second tree
    num_red_second_tree = 0.5 * 20  # 50% of 20 apples

    # Calculate the total number of red apples harvested
    total_red_apples = num_red_first_tree + num_red_second_tree
    result = total_red_apples
    return result

print(solution())