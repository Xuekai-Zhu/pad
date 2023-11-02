def solution():
    """The last time Bob cut his hair he cut it to 6 inches. His hair is now 36 inches long. If hair grows at a rate of .5 inches per month how many years did it take him to grow out his hair?"""
    # Define the initial hair length and the desired hair length
    INITIAL_LENGTH = 6
    DESIRED_LENGTH = 36

    # Define the hair growth rate in inches per month
    GROWTH_RATE = 0.5

    # Calculate the difference in hair length and the number of months needed to grow that amount
    length_difference = DESIRED_LENGTH - INITIAL_LENGTH
    months = length_difference / GROWTH_RATE

    # Convert the number of months to years
    years = months / 12

    # Return the result
    result = years
    return result

print(solution())