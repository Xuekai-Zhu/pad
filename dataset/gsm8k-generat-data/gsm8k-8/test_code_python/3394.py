def solution():
    # Calculate the total amount of sand for Cities A, B, and C
    total_ABC = 16.5 + 26 + 24.5

    # Calculate the amount of sand for City D
    cityD = 95 - total_ABC
    result = cityD
    return result

print(solution())