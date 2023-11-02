def solution():
    total_flowers = 44
    yellow_white = 13
    red_yellow = 17
    red_white = 14

    # Calculate the number of flowers that are only red
    red_only = total_flowers - (yellow_white + red_yellow + red_white)

    # Calculate the difference between the number of flowers that are red and the number of flowers that are white
    difference = (red_only + red_yellow + red_white) - (yellow_white + red_yellow + red_white)
    result = difference
    return result

print(solution())