def solution():
    # Calculate the number of women on the airplane
    num_women = 80 / 2 - 30

    # Calculate the number of children on the airplane
    num_children = 80 - 30 - num_women

    result = num_children
    return result

print(solution())