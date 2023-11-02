def solution():
    # Set the initial number of plants
    num_plants = 20 / 2**3 + 4

    # Calculate the initial number of plants
    for i in range(3):
        num_plants *= 2

    initial_plants = num_plants + 4
    result = initial_plants
    return result

print(solution())