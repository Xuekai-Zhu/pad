def solution():
    # Number of silverware Stephanie needs for herself
    num_silverware = 5

    # Number of extra silverware Stephanie needs for guests
    num_extra_silverware = 10

    # Total number of silverware needed
    total_silverware = (num_silverware + num_extra_silverware) * 4

    # Adjusted number of silverware to fit in drawer
    adjusted_silverware = (num_silverware - 4) + (num_extra_silverware - 4) + \
                          (num_silverware - 5) + (num_extra_silverware - 3)

    result = total_silverware + adjusted_silverware
    return result

print(solution())