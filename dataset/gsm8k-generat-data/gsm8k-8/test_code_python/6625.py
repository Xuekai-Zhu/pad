def solution():
    # Calculate the total number of apples needed for full-size pies
    full_size_apples = 48

    # Calculate the total number of apples needed for mini pies
    mini_pie_apples = 24 * 0.5

    # Calculate the number of leftover apples
    leftover_apples = full_size_apples - mini_pie_apples

    result = leftover_apples
    return result

print(solution())