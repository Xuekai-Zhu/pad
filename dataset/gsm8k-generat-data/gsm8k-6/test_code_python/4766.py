def solution():
    # Calculate the amount of sugar harvested by the ants in three hours
    harvested_sugar = 4 * 3  # every hour, the ants remove 4 ounces of sugar

    # Calculate the remaining sugar in the bag after three hours
    remaining_sugar = 24 - harvested_sugar

    # Calculate how many more hours the ants will need to harvest the remaining sugar
    hours_needed = remaining_sugar / 4  # every hour, the ants remove 4 ounces of sugar
    result = hours_needed
    return result

print(solution())