def solution():
    # Calculate the number of men
    men = 120 / 3

    # Calculate the number of women
    women = 120 / 2

    # Calculate the number of children
    children = 120 - men - women

    result = children
    return result

print(solution())