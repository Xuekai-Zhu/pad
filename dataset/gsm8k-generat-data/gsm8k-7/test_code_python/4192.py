def solution():
    num_red_chairs = 5
    num_yellow_chairs = 4 * num_red_chairs
    num_blue_chairs = num_yellow_chairs - 2

    # Calculate the total number of chairs
    total_chairs = num_red_chairs + num_yellow_chairs + num_blue_chairs
    result = total_chairs
    return result

print(solution())