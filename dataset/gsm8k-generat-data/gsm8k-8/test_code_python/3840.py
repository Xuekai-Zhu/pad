def solution():
    # Calculate the number of green marbles
    green_marbles = 38 / 2

    # Calculate the total number of red and green marbles
    red_and_green = 38 + green_marbles

    # Calculate the number of dark blue marbles
    dark_blue = 63 - red_and_green

    result = dark_blue
    return result

print(solution())