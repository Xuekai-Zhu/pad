def solution():
    num_red = 12
    num_brown = 6
    num_green = 14
    num_blue = 6

    # Calculate the number of white-spotted red mushrooms
    white_spotted_red = 2/3 * num_red

    # Calculate the number of white-spotted brown mushrooms
    white_spotted_brown = num_brown

    # Calculate the number of white-spotted blue mushrooms
    white_spotted_blue = 1/2 * num_blue

    # Calculate the total number of white-spotted mushrooms
    total_white_spotted = white_spotted_red + white_spotted_brown + white_spotted_blue
    result = total_white_spotted
    return result

print(solution())