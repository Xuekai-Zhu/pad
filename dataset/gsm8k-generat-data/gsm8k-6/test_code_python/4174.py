def solution():
    # Calculate the coal capacity of each boxcar
    blue_boxcar_capacity = 2 * 4000  # black boxcars can hold half as much as blue boxcars
    red_boxcar_capacity = 3 * blue_boxcar_capacity  # red boxcars can hold 3 times as much as blue boxcars

    # Calculate the total coal capacity of all the boxcars
    total_coal_capacity = 3 * red_boxcar_capacity + 4 * blue_boxcar_capacity + 7 * 4000

    result = total_coal_capacity
    return result

print(solution())