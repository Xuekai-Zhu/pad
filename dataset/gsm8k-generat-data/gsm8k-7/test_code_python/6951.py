def solution():
    # Let x be the amount of storage space on the second floor
    # Then the amount of storage space on the first floor is 2x
    # The total amount of storage space is 3x
    # The boxes took up 1/4 of the second floor space, so:
    x = 5000 / 0.25
    total_space = 3 * x
    used_space = 5000
    available_space = total_space - used_space
    result = available_space
    return result

print(solution())