def solution():
    # Define the fractions of each color marble
    blue_fraction = 0.5
    red_fraction = 0.25
    green_fraction = 27 / total_marbles
    yellow_fraction = 14 / total_marbles

    # Set up an equation to solve for total_marbles
    equation = blue_fraction + red_fraction + green_fraction + yellow_fraction
    total_marbles = 1 / equation

    result = total_marbles
    return result

print(solution())