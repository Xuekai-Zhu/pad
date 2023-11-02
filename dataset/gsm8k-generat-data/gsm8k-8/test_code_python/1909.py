def solution():
    # Calculate the number of kids who finish in less than 6 minutes
    less_than_6 = 0.1 * 40

    # Calculate the number of kids who finish in less than 8 minutes
    less_than_8 = 3 * less_than_6

    # Calculate the number of kids who finish between 8 and 14 minutes
    between_8_and_14 = 40 - less_than_6 - less_than_8

    # Calculate the number of kids who take more than 14 minutes
    more_than_14 = (1/6) * between_8_and_14

    result = more_than_14
    return result

print(solution())