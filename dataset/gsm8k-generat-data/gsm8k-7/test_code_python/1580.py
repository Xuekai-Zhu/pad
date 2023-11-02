def solution():
    num_rows = 6
    flowers_per_row = 13

    # Calculate the total number of flowers in the garden
    total_flowers = num_rows * flowers_per_row

    # Calculate the total number of yellow flowers
    num_yellow = 12

    # Calculate the total number of green flowers
    num_green = num_yellow * 2

    # Calculate the total number of red flowers
    num_red = total_flowers - num_yellow - num_green

    result = num_red
    return result

print(solution())