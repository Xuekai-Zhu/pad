def solution():
    # Calculate the number of white-spotted red mushrooms
    white_spotted_red = (2/3) * 12

    # Calculate the number of white-spotted brown mushrooms
    white_spotted_brown = 6

    # Calculate half the number of blue mushrooms
    half_blue = 0.5 * 6

    # Calculate the total number of white-spotted mushrooms
    total_white_spotted = white_spotted_red + white_spotted_brown + half_blue

    result = total_white_spotted
    return result

print(solution())