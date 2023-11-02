def solution():
    black_capacity = 4000
    blue_capacity = 2 * black_capacity
    red_capacity = 3 * blue_capacity

    # Calculate the total capacity of all black boxcars
    total_black_capacity = 7 * black_capacity

    # Calculate the total capacity of all blue boxcars
    total_blue_capacity = 4 * blue_capacity

    # Calculate the total capacity of all red boxcars
    total_red_capacity = 3 * red_capacity

    # Calculate the total capacity of all boxcars
    total_capacity = total_black_capacity + total_blue_capacity + total_red_capacity
    result = total_capacity
    return result

print(solution())