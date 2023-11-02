def solution():
    num_siblings = 14
    kay_age = 32

    # Calculate the age of the youngest sibling
    youngest = (1/2) * kay_age - 5

    # Calculate the age of the oldest sibling
    oldest = 4 * youngest

    result = oldest
    return result

print(solution())