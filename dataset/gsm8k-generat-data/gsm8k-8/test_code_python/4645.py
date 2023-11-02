def solution():
    # Calculate the number of red and blue marbles
    red_blue = (50 - 20) / 2

    # Calculate the number of marbles Jack removes
    diff_wb = abs(20 - red_blue)
    removal = 2 * diff_wb

    # Calculate the number of marbles left in the box
    marbles_left = 50 - removal
    result = marbles_left
    return result

print(solution())