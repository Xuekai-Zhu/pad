def solution():
    # Define initial values
    bags1 = 12
    weight1 = 24
    bags2 = 8

    # Use proportions to solve for weight2
    weight2 = (bags2 * weight1) / bags1
    result = weight2
    return result

print(solution())