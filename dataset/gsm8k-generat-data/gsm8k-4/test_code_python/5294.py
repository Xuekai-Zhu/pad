def solution():
    """Allie picked 44 wildflowers. Thirteen of the flowers were yellow and white, seventeen of the flowers were red and yellow, and 14 of the flowers were red and white. How many more flowers contained the color red than contained the color white?"""
    # Calculate the total number of flowers that were either yellow, red, or white
    yellow_white = 13
    red_yellow = 17
    red_white = 14

    total_yr = yellow_white + red_yellow
    total_rw = red_white + yellow_white
    total_yw = yellow_white + red_white

    total_flowers = total_yr + total_rw + total_yw

    # Calculate the number of flowers that were either red or white
    red_or_white = total_rw + total_yw

    # Calculate the number of flowers that were red
    red = red_or_white - yellow_white

    # Calculate the number of flowers that were white
    white = red_or_white - red_white

    # Calculate the difference between the number of red flowers and white flowers
    difference = red - white

    # return the result
    result = difference
    return result

print(solution())