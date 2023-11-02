def solution():
    num_blue_chairs = 10
    num_green_chairs = num_blue_chairs * 3
    num_white_chairs = (num_blue_chairs + num_green_chairs) - 13

    # Calculate the total number of chairs
    total_chairs = num_blue_chairs + num_green_chairs + num_white_chairs
    result = total_chairs
    return result

print(solution())