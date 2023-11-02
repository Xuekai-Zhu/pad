def solution():
    # Calculate the number of kids who finish in less than 6 minutes
    less_than_6 = 0.1 * 40  # 10% of 40

    # Calculate the number of kids who finish in less than 8 minutes
    less_than_8 = 3 * less_than_6

    # Calculate the number of kids who take more than 14 minutes
    remaining = 40 - less_than_6 - less_than_8
    more_than_14 = remaining / 6

    result = more_than_14
    return result

print(solution())