def solution():
    num_brownies = 20

    # Give half of the brownies to the school administrator
    num_brownies = num_brownies / 2

    # Give half of the remaining brownies to Carl
    num_brownies = num_brownies / 2

    # Give 2 of the remaining brownies to Simon
    num_brownies = num_brownies - 2

    result = num_brownies
    return result

print(solution())