def solution():
    num_red = 38
    num_green = num_red / 2  # half as many green marbles
    num_total = 63

    # Calculate the number of dark blue marbles
    num_dark_blue = num_total - num_red - num_green
    result = num_dark_blue
    return result

print(solution())