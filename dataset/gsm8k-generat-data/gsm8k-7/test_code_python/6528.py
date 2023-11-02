def solution():
    num_tomatoes = 2073
    num_corn = 4112
    num_onions = 985

    # Calculate the total number of onions from tomatoes and corn
    total_onions = num_tomatoes + num_corn

    # Calculate the difference between the total onions and num_onions
    difference = total_onions - num_onions
    result = difference
    return result

print(solution())