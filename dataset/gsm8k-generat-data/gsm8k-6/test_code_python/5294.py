def solution():
    # Calculate the number of flowers containing the color red and white
    red_and_white = 13 + 17 + 14  # number of flowers that are either red and white
    red_only = 44 - red_and_white  # number of flowers that are only red
    white_only = 44 - red_and_white  # number of flowers that are only white

    # Calculate the difference between the number of red flowers and white flowers
    red_vs_white = red_only - white_only
    result = red_vs_white
    return result

print(solution())