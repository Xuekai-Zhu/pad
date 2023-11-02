def solution():
    # Define the capacities of each color boxcar
    blue_capacity = 8000
    black_capacity = 4000
    red_capacity = 3 * blue_capacity

    # Calculate the total capacity of all boxcars
    total_capacity = 3 * red_capacity + 4 * blue_capacity + 7 * black_capacity

    result = total_capacity
    return result

print(solution())