def solution():
    num_cars = 20
    fraction_donated = 1/4

    # Calculate the number of cars donated
    num_donated = num_cars * fraction_donated

    # Calculate the number of cars left
    num_left = num_cars - num_donated
    result = num_left
    return result

print(solution())