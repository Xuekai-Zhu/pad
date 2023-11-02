def solution():
    """Kate has 2 red balloons and 4 blue balloons. Assuming she inflates 4 more balloons, two of each color red and blue, what is the percent likelihood that one selected at random will be red?"""
    # Define the initial number of red and blue balloons
    initial_red = 2
    initial_blue = 4

    # Define the number of balloons inflated
    inflated_red = 2
    inflated_blue = 2

    # Calculate the total number of red and blue balloons
    total_red = initial_red + inflated_red
    total_blue = initial_blue + inflated_blue

    # Calculate the probability of selecting a red balloon
    prob_red = total_red / (total_red + total_blue) * 100

    # return the result
    result = prob_red
    return result

print(solution())