def solution():
    # Calculate the number of full-size pies Ivan was originally planning to make
    full_size_pies = 24

    # Calculate the number of apples needed for the full-size pies
    apples_full_size = full_size_pies * 2

    # Calculate the total number of apples used for the 24 mini pies
    apples_mini_pies = 24 * 1/2

    # Calculate the number of leftover apples
    leftover_apples = apples_full_size - apples_mini_pies

    result = leftover_apples
    return result

print(solution())