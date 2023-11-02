def solution():
    """Kate has 2 red balloons and 4 blue balloons. Assuming she inflates 4 more balloons, two of each color red and blue, what is the percent likelihood that one selected at random will be red?"""
    # Define the number of red and blue balloons after inflating
    red_balloons = 2 + 2
    blue_balloons = 4 + 2

    # Calculate the total number of balloons
    total_balloons = red_balloons + blue_balloons

    # Calculate the percentage chance of selecting a red balloon
    red_chance = (red_balloons / total_balloons) * 100

    # Display the percentage chance of selecting a red balloon
    result = red_chance
    return result

print(solution())