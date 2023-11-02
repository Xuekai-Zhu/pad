def solution():
    # Calculate the number of kids who finish in less than 6 minutes
    less_than_6 = round(0.1 * 40)

    # Calculate the number of kids who finish in less than 8 minutes
    less_than_8 = 3 * less_than_6

    # Calculate the number of kids who finish in more than 8 minutes
    more_than_8 = 40 - less_than_6 - less_than_8

    # Calculate the number of kids who take more than 14 minutes
    more_than_14 = round((1/6) * more_than_8)

    result = more_than_14
    return result

print(solution())