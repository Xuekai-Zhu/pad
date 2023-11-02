def solution():
    # Calculate how many cakes Julia bakes each day
    cakes_per_day = 5 - 1

    # Initialize the number of cakes Julia has left
    cakes_left = cakes_per_day * 6

    # Subtract one cake every other day
    for day in range(1, 7):
        if day % 2 == 0:
            cakes_left -= 1

    result = cakes_left
    return result

print(solution())