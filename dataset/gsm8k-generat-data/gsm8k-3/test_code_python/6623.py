def solution():
    """Farmer Steven needs to load his truck up with compost.  His tractor can scoop up compost at a rate of 75 pounds per minute.  Steven's son, Darrel, wants to help.  Using a shovel, Darrel can scoop up 10 pounds per minute.  How much time, in minutes, would it take for the two working together at the same time to load up 2550 pounds of compost into the truck?"""
    # Define the rate at which Steven's tractor can scoop up compost
    STEVEN_RATE = 75

    # Define the rate at which Darrel can scoop up compost
    DARREL_RATE = 10

    # Define the total amount of compost to be loaded
    TOTAL_COMPOST = 2550

    # Calculate the combined rate at which Steven and Darrel can scoop up compost
    COMBINED_RATE = STEVEN_RATE + DARREL_RATE

    # Calculate the amount of time it would take for Steven and Darrel to load up the compost
    time = TOTAL_COMPOST / COMBINED_RATE

    # Display the amount of time in minutes
    result = time
    return result

print(solution())