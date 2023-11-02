def solution():
    """Farmer Steven needs to load his truck up with compost. His tractor can scoop up compost at a rate of 75 pounds per minute. Steven's son, Darrel, wants to help. Using a shovel, Darrel can scoop up 10 pounds per minute. How much time, in minutes, would it take for the two working together at the same time to load up 2550 pounds of compost into the truck?"""
    # Define the compost weight and the scoop rates of Steven and Darrel
    compost_weight = 2550
    steven_rate = 75
    darrel_rate = 10

    # Calculate the combined rate of Steven and Darrel
    combined_rate = steven_rate + darrel_rate

    # Calculate the time it will take for Steven and Darrel to load up the compost
    time = compost_weight / combined_rate

    # round to the nearest minute
    result = round(time)
    return result

print(solution())