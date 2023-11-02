def solution():
    total_flowers = 44
    yellow_white = 13
    red_yellow = 17
    red_white = 14

    # Calculate the number of flowers that contain red
    red_count = red_yellow + red_white

    # Calculate the number of flowers that contain white
    white_count = yellow_white + red_white

    # Calculate the difference between the number of red flowers and white flowers
    difference = red_count - white_count
    result = difference
    return result

print(solution())