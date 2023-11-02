def solution():
    num_brownies = 2 * 12  # Mother made 2 dozen brownies
    num_brownies -= 8  # Father ate 8 of them
    num_brownies -= 4  # Mooney ate 4 of them

    num_brownies += 2 * 12  # Mother made another two dozen brownies the next morning

    result = num_brownies
    return result

print(solution())